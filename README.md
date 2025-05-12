# Discord Controlled Vibrator
Yes its exactly what it says.

## Description

You use a Raspberry Pi to control a motor using PWM. Means of driving the motor is up to your circuits. I personally used a L293D to drive a MOSFET to prevent burning (its very stupid but this project is stupid enough)..\
The vibrator used is a DIY rotor however if you have access to the motor terminals and are able to drive it using your own circuit. This code can work.\
The bot only provides a PWM signal and enable signal out the GPIO pins (GPIO18 (Pin12) and GPIO21 (Pin40) were used)
- GPIO18 (Pin12) is used for the PWM signal
- GPIO21 (Pin40) is used for an enable signal
## Installation (why?)
- Clone this repository.
- Then install the required dependancies
```
pip install -r requirements.txt
```
- (This really depends on your installation of python)
- Open the `main.py` file to add your bot token and perfer parameters
- Finally, profit. Don't make a mess UwU~
  
This was tested using Python 3.10.10
