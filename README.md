**Flowshield**

# Description
Flowshield is a physical device that measures bladder volume from impedance changes from the body. The physical device is a belt that wraps
around a person's lower abdomen and uses bioimpedance analysis to send and measure electrical signals from the body. In the models folder there
is a slx file. The Flowshield_Prototypefinal.slx file is a MATLAB Simulink model that simulates bladder volume based on the logic of a water tank
differential equation. A two page GUI has been constructed to show the results of the Simulink model to the user.

## Directions for running Simulink model.
** Disclaimer the version of MATLAB that is used is 25.1.0.2973910.
1. To install the MATLAB Simulink model you have to have MATLAB installed.
2. Then download the Flowshield_Prototype.slx file.
3. Click on the downloaded .slx file and it should open in MATLAB.
4. In order to run the Simulink model you have to set the initial volume which is in the block.
5. Once this block is clicked click on the minimum and change it to mL. The maximum bladder volume currently set is 700mL based on prior research.
6. After the initial parameters are set run the model with the run button the top of the page or press Ctrl + T.

### Directions for running the GUI
** Disclaimer the version of Python that can be used is Python 3.12.16 or less. Python 3.13 and up will not work. This is due to the MATLAB version currently being used.
1. Dowload Pyside6 Qt Designer
2. Fork or Clone this repository to have access to all necessary files.
3. A virtual environment has been created to be able to use the right version of Python to run the GUI.
4. To activate the virtual environment run this code in the terminal **c:/(The folder where Flowshield is downloaded locally)/.venv/Scripts/Activate.ps1**
5. Now that the virtual environment is activated you can now run the GUI from your terminal with the command **python main.py**
