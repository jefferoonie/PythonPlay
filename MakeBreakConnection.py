# Testing out making, and breaking a connection, on GPIO.
# Testing for possible reed switch usage.
# - Connect GPIO to ground = "Closed"
# - Disconnected GPIO from ground = "Open"

import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

reed1 = 12

GPIO.setup(reed1, GPIO.IN, GPIO.PUD_UP)

while True:
    if GPIO.input(reed1) == False:
        print("Reed is closed.")
    else:
        if GPIO.input(reed1) == True:
            print("Reed is open.")
GPIO.cleanup()
