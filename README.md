# **Flowshield**

## Description
Flowshield is a wearable device under development that estimates bladder volume from bioimpedance (BioZ) measurements taken with a belt around the lower abdomen. This repository contains the software prototype: a MATLAB Simulink model of filling and voiding with alert states, and a two-page Python GUI that runs the model and displays results. BioZ hardware (MAX30009 evaluation kit, electrodes, belt) has not been integrated yet.

The Simulink model ('models/Flowshield_Prototypefinal.slx') simulates bladder volume using a differential equation (dV/dt = Q_in - Q_out) with Stateflow logic for the Normal, Warning (300mL) , and Urgent (600mL) alert states and for voiding.

## Repository Structure
```
Flowshield/
├── main.py
├── requirements.txt
├── README.md
├── gui/          (flowshield.ui, flowshield_ui.py, main_window.py)
├── simulation/   (matlab_interface.py)
└── models/       (Flowshield_Prototypefinal.slx)
```

## Running the Simulink Model on Its Own
Note: developed with MATLAB 25.1.0.2973910 (R2025a), with Simulink and Stateflow installed.
1. Clone this repository.
2. Open `models/Flowshield_Prototypefinal.slx` in MATLAB.
3. Double-click the `V_t` integrator block and set **Initial condition** to the starting bladder volume in mL.
4. Run the model with the Run button or Ctrl + T.

The model logs `bladder_volume`, `urgent`, `warning`, and `void_event`. The GUI reads these signals by name, so keep the names if you edit the model. When you use the GUI, it sets the initial volume for you.

## Running the GUI
Note: the Python version must be supported by your MATLAB release. For R2025a, use Python 3.12 or lower. Python 3.13 and up will not work.
1. Install MATLAB R2025a with Simulink and Stateflow.
2. Clone this repository.
3. In the repository folder, create and activate a virtual environment (PowerShell):
   ```
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```
4. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the GUI from the repository folder:
   ```
   python main.py
   ```

The first simulation takes longer (10-30 seconds) because MATLAB starts on the first run.

Optional: install Qt Designer (included with PySide6 tools) only if you want to edit `gui/flowshield.ui`.

