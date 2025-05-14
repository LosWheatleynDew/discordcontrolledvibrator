# Discord Controlled Vibrator
Yes its exactly what it says.\
If you want someone to control your DIY vibrator but they're hundreds of kilometers(miles) away from you. This program is perfect for you
## Description

You use a Raspberry Pi to control a motor using PWM. Means of driving the motor is up to your circuits. I personally used a L293D to drive a MOSFET to prevent burning (its very stupid but this project is stupid enough)..\
The vibrator used is a DIY rotor however if you have access to the motor terminals and are able to drive it using your own circuit. This code can work.\
The bot only provides a PWM signal and enable signal out the GPIO pins (GPIO12 (Pin32) and GPIO21 (Pin40) were used)
- GPIO12 (Pin32) is used for the PWM signal
- GPIO21 (Pin40) is used for an enable signal

### Commands used:
- `-=letsplay` (Allows ANY user to start controlling ur vibrator)
- `-=tease` (Only allows YOU to start)
- `-=onigiri` (**SAFE WORD** Use this to stop the vibrator and delete the remote)
## Images
![image](https://github.com/user-attachments/assets/20f55327-1d8e-4754-89e8-6e69e75d823d)
![image](https://github.com/user-attachments/assets/f91bda79-507e-4947-9654-c342899ac40a)
![image](https://github.com/user-attachments/assets/18c8eabf-9039-4315-8cbd-818627f24c62)


## Installation (why?)
- Clone this repository.
- Then install the required dependancies
```
pip install -r requirements.txt
```
- Open the `main.py` file to add your bot token and perfer parameters
- Finally, profit. Don't make a mess UwU~
  
This was tested using Python 3.10.10 on a raspberry pi 5. Using the L293D chip to drive the motor
