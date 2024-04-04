import grovepi # check the file on the pi!
import time

try:
    while True:
        try: 
            mag = grovepi.analog_read(15)
            ir = grovepi.analog_read(16)
        except:
            print("Error")
except: 
    print("Terminating")