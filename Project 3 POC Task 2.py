import time
import brickpi3

BP = brickpi3.BrickPi3()
constant = 3

startTime = time.time()
BP.set_motor_dps(BP.PORT_B, -100)
BP.set_motor_dps(BP.PORT_C, 100)
while (startTime + constant > time.time()):
    time.sleep(0.1)
BP.reset_all()
