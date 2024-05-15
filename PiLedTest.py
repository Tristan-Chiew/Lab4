from hal import hal_led as led
from hal import hal_input_switch as switch
import time

led.init()
switch.init()

delay = 0.2
delay2 = 0.1
toggle = 0

while True:
    if switch.read_slide_switch() == 0:
        end_time = time.time() + 5  
        print(time.time())
        print(end_time, "\n")
        while time.time() <= end_time and toggle == 0:

            led.set_output(0, 1)
            time.sleep(delay2)
            print("LED")
            led.set_output(0, 0)
            time.sleep(delay2)
        toggle = 1
        led.set_output(0, 0)
        time.sleep(delay2)

    else:
        print("in left pos")
        led.set_output(0, 1)
        time.sleep(delay)
        led.set_output(0, 0)
        time.sleep(delay)
        toggle = 0
