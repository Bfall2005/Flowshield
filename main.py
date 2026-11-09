import sys
from PySide6.QtWidgets import QApplication
from gui.main_window import FlowShieldGUI
from simulation.matlab_interface import shutdown


def main():
    # Initialize the PySide6 application
    app = QApplication(sys.argv)

    # Close the MATLAB engine cleanly when the window is closed
    app.aboutToQuit.connect(shutdown)

    # Create the FlowShield GUI
    window = FlowShieldGUI()

    # Display the GUI
    window.show()

    # Start the application event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()