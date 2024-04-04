import time
import brickpi3
import grovepi

BP = brickpi3.BrickPi3()
ultrasonics = [4, 3, 2] # ultrasonic sensors, left to right from vehicle's perspective
motors = [BP.PORT_B, BP.PORT_C] # left, right

try:
    turnDistance = 5
    while True:
        oneUltraReading = []
        for ultrasonic in ultrasonics:
            oneUltraReading.append(grovepi.ultrasonicRead(ultrasonic))
        if (oneUltraReading[1] > turnDistance):
            BP.set_motor_dps(motors[0], 100)
            BP.set_motor_dps(motors[1], 100)
        elif (oneUltraReading[0] > 10):
            BP.set_motor_dps(motors[0], 100)
            BP.set_motor_dps(motors[1], -100)
        else:
            BP.set_motor_dps(motors[0], -100)
            BP.set_motor_dps(motors[1], 100)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Ending")
BP.reset_all()

