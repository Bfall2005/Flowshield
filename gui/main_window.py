import sys
from pathlib import Path

from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QMessageBox
)
from PySide6.QtUiTools import QUiLoader

from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

from simulation.matlab_interface import run_simulation


# Must match the items in the Duration dropdown in flowshield.ui exactly
DURATION_OPTIONS = {
    "1 min": 60,
    "5 min": 300,
    "10 min": 600,
    "30 min": 1800,
    "1 hour": 3600,
    "2 hours": 7200,
    "5 hours": 18000,
    "10 hours": 36000,
    "24 hours": 86400,
}


class SimulationWorker(QObject):
    #Runs MATLAB/Simulink off the GUI thread so the window doesn't freeze.

    finished = Signal(dict)
    failed = Signal(str)

    def __init__(self, duration, initial_volume):
        super().__init__()
        self.duration = duration
        self.initial_volume = initial_volume

    def run(self):
        try:
            results = run_simulation(
                duration=self.duration,
                initial_volume=self.initial_volume
            )
            self.finished.emit(results)
        except Exception as error:
            self.failed.emit(str(error))


class FlowShieldGUI:

    def __init__(self):
        #Load GUI interface from Qt Designer .ui file
        ui_path = Path(__file__).resolve().parent / "flowshield.ui"

        loader = QUiLoader()
        self.window = loader.load(str(ui_path))

        if self.window is None:
            raise RuntimeError("Failed to load FlowShield GUI")

        #Access stacked packages
        self.pages = self.window.stackedWidget

        #Access GUI buttons
        self.btn_run_simulation = self.window.btnRunSimulation
        self.btn_back = self.window.btnBack
        self.btn_run_again = self.window.btnRun

        #Connect button functionality
        self.btn_run_simulation.clicked.connect(self.run_simulation)
        self.btn_back.clicked.connect(self.back_to_setup)
        self.btn_run_again.clicked.connect(self.run_again)

        #Initialize MATLAB graph
        self.figure = Figure(figsize=(6, 4))
        self.canvas = FigureCanvasQTAgg(self.figure)

        graph_layout = QVBoxLayout(self.window.graphContainer)
        graph_layout.setContentsMargins(5, 5, 5, 5)
        graph_layout.addWidget(self.canvas)

        #Worker thread bookkeeping
        self.thread = None
        self.worker = None
        self.duration_text = ""
        self._run_button_text = self.btn_run_simulation.text()

        #Start Configuration Page
        self.pages.setCurrentIndex(0)

    def run_simulation(self):

        #Read Page 1 inputs
        initial_volume_input = self.window.spinInitialVolume.value()
        self.duration_text = self.window.comboDuration.currentText()

        if self.duration_text not in DURATION_OPTIONS:
            QMessageBox.warning(
                self.window,
                "Invalid Duration",
                "Please select a valid simulation duration."
            )
            return

        duration = DURATION_OPTIONS[self.duration_text]

        print(f"Selected initial volume: {initial_volume_input} mL")
        print(f"Selected duration: {duration} seconds")

        #Run MATLAB/Simulink worker thread
        self.btn_run_simulation.setEnabled(False)
        self.btn_run_simulation.setText("Running simulation...")

        self.thread = QThread()
        self.worker = SimulationWorker(duration, initial_volume_input)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.on_simulation_finished)
        self.worker.failed.connect(self.on_simulation_failed)

        # Clean up the thread once the worker reports back
        self.worker.finished.connect(self.thread.quit)
        self.worker.failed.connect(self.thread.quit)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    def on_simulation_finished(self, results):

        self._reset_run_button()

        #Update Page 2 labels with results from MATLAB/Simulink
        self.window.lblInitialVolume.setText(
            f"{results['initial_volume']:.1f} mL"
        )

        self.window.lblFinalVolume.setText(
            f"{results['final_volume']:.1f} mL"
        )

        # Final alert from the Stateflow output.
        alert_text = results["final_alert"]
        if results["peak_alert"] != results["final_alert"]:
            alert_text += f" (peak: {results['peak_alert']})"
        self.window.lblAlertStatus.setText(alert_text)

        self.window.lbltime.setText(self.duration_text)

        # Filling / Voiding from the Bladder_Controller void_event signal
        self.window.label_18.setText(results["state"])

        # Time to Urgent is in results["time_to_urgent"] (seconds, or None).
        # Put it on whichever label you want, for example:
        # t = results["time_to_urgent"]
        # self.window.lbltime.setText("Not reached" if t is None else f"{t:.0f} s")

        #Update Matplotlib graph with results
        self.update_graph(results)

        #Switch to Results page
        self.pages.setCurrentIndex(1)

    def on_simulation_failed(self, message):

        self._reset_run_button()

        QMessageBox.critical(
            self.window,
            "Simulation Error",
            f"MATLAB/Simulink failed:\n{message}"
        )

    def _reset_run_button(self):
        self.btn_run_simulation.setEnabled(True)
        self.btn_run_simulation.setText(self._run_button_text)

    def update_graph(self, results):

        times = results["times"]
        volumes = results["volumes"]

        # Clear previous graph
        self.figure.clear()

        ax = self.figure.add_subplot(111)

        # Plot bladder volume
        ax.plot(
            times,
            volumes,
            color="#087F8C",
            linewidth=2,
            label="Bladder Volume"
        )

        # Warning threshold
        ax.axhline(
            300,
            color="orange",
            linestyle="--",
            label="Warning (300 mL)"
        )

        # Urgent threshold
        ax.axhline(
            600,
            color="red",
            linestyle="--",
            label="Urgent (600 mL)"
        )

        # Graph formatting
        ax.set_title("FlowShield Bladder Volume Simulation")
        ax.set_xlabel("Time (seconds)")
        ax.set_ylabel("Bladder Volume (mL)")

        ax.legend()
        ax.grid(True, alpha=0.3)

        self.figure.tight_layout()
        self.canvas.draw()

    def back_to_setup(self):
        self.pages.setCurrentIndex(0)

    def run_again(self):
        # Rerun the simulation with the same parameters
        self.run_simulation()

    def show(self):
        self.window.show()


# Optional standalone testing for GUI
def main():
    app = QApplication(sys.argv)

    gui = FlowShieldGUI()
    gui.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()