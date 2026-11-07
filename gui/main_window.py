
import sys
from pathlib import Path

from PySide6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QMessageBox
)
from PySide6.QtUiTools import QUiLoader

from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

from simulation.matlab_interface import run_simulation


class FlowShieldGUI:

    def __init__(self):

        # ----------------------------------
        # 1. Load the Qt Designer interface
        # ----------------------------------
        ui_path = Path(__file__).resolve().parent / "flowshield.ui"

        loader = QUiLoader()
        self.window = loader.load(str(ui_path))

        if self.window is None:
            raise RuntimeError("Failed to load FlowShield GUI")

        # ----------------------------------
        # 2. Access the stacked pages
        # ----------------------------------
        self.pages = self.window.stackedWidget

        # ----------------------------------
        # 3. Access GUI buttons
        # ----------------------------------
        self.btn_run_simulation = self.window.btnRunSimulation
        self.btn_back = self.window.btnBack
        self.btn_run_again = self.window.btnRun

        # ----------------------------------
        # 4. Connect button functionality
        # ----------------------------------
        self.btn_run_simulation.clicked.connect(self.run_simulation)
        self.btn_back.clicked.connect(self.back_to_setup)
        self.btn_run_again.clicked.connect(self.run_again)

        # ----------------------------------
        # 5. Initialize Matplotlib graph
        # ----------------------------------
        self.figure = Figure(figsize=(6, 4))
        self.canvas = FigureCanvasQTAgg(self.figure)

        graph_layout = QVBoxLayout(self.window.graphContainer)
        graph_layout.setContentsMargins(5, 5, 5, 5)
        graph_layout.addWidget(self.canvas)

        # ----------------------------------
        # 6. Start on configuration page
        # ----------------------------------
        self.pages.setCurrentIndex(0)

    def run_simulation(self):

        # ----------------------------------
        # 1. Read Page 1 inputs
        # ----------------------------------
        initial_volume_input = self.window.spinInitialVolume.value()
        duration_text = self.window.comboDuration.currentText()

        duration_options = {
            "1 minute": 60,
            "30 minutes": 1800,
            "1 hour": 3600,
            "2 hours": 7200
        }

        if duration_text not in duration_options:
            QMessageBox.warning(
                self.window,
                "Invalid Duration",
                "Please select a valid simulation duration."
            )
            return

        duration = duration_options[duration_text]

        print(f"Selected initial volume: {initial_volume_input} mL")
        print(f"Selected duration: {duration} seconds")

        # ----------------------------------
        # 2. Run MATLAB/Simulink
        # ----------------------------------
        try:
            results = run_simulation(duration=duration)

        except Exception as error:
            QMessageBox.critical(
                self.window,
                "Simulation Error",
                f"MATLAB/Simulink failed:\n{error}"
            )
            return

        # ----------------------------------
        # 3. Extract simulation results
        # ----------------------------------
        initial_volume = results["initial_volume"]
        final_volume = results["final_volume"]

        # ----------------------------------
        # 4. Determine alert state
        # ----------------------------------
        if final_volume >= 600:
            alert = "Urgent"
        elif final_volume >= 300:
            alert = "Warning"
        else:
            alert = "Normal"

        # ----------------------------------
        # 5. Update Page 2 summary labels
        # ----------------------------------
        self.window.lblInitialVolume.setText(
            f"{initial_volume:.1f} mL"
        )

        self.window.lblFinalVolume.setText(
            f"{final_volume:.1f} mL"
        )

        self.window.lblAlertStatus.setText(alert)

        self.window.lblDuration.setText(duration_text)

        # Bladder mode is not yet retrieved from Simulink
        self.window.lblBladderState.setText("Not available")

        # ----------------------------------
        # 6. Update Matplotlib graph
        # ----------------------------------
        self.update_graph(results)

        # ----------------------------------
        # 7. Switch to results page
        # ----------------------------------
        self.pages.setCurrentIndex(1)

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
        # Return to configuration page
        self.pages.setCurrentIndex(0)

    def show(self):
        self.window.show()


# Optional standalone testing
def main():
    app = QApplication(sys.argv)

    gui = FlowShieldGUI()
    gui.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
