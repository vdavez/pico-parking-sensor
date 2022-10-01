import machine
from np import NP
import time
import vl53l1x

# Initialize LEDs
leds = NP(6,28)

# Initialize Time of Flight Sensor
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
tof = vl53l1x.VL53L1X(i2c)

counter = 0

while True:
    distance = tof.read()
    if distance > 3000:
        leds.clear()
        counter = 0
    elif distance > 1150:
        counter = 0
        leds.set_hls_color(0.33333,0.5,1.0)
    elif distance > 750:
        counter = 0
        leds.set_hls_color(0.15,0.5,1.0)
    elif distance > 550:
        counter = 0
        leds.set_hls_color(0.08333,0.5,1.0)
    else:
        counter += 1
        if counter < 30:
            leds.set_hls_color(0.0,0.5,1.0)
        else:
            leds.clear()
    time.sleep(1)