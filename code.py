# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Julianne Leblanc-Peltier
# April 2025
#
# Move a servo with a potentiometer in sync

import time
import board
import pwmio
import servo
from analogio import AnalogIn

# create a PWMOut object on Pin 16.
pwm = pwmio.PWMOut(board.GP16, duty_cycle=2 ** 15, frequency=50)

potentionmeter = AnalogIn(board.GP26) # sets pot pin to pin 26/A0

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm, min_pulse = 650, max_pulse = 2500)

while True:
    print((potentionmeter.value))
    potVal = potentionmeter.value

    # shows value of the potentiometer
    print(potVal)

    # changes range from 0-65535 to 0-180
    angle = potVal * (180/65535)
    my_servo.angle = angle
    time.sleep(1)
