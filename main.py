import machine
from np import NP
import time
import vl53l1x

# Initialize LEDs
leds = NP(6,28)

# Initialize Time of Flight Sensor
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
tof = vl53l1x.VL53L1X(i2c)

while True:
    distance = tof.read()
    print(distance)
    if distance > 1000:
        leds.clear()
    elif distance > 500:
        leds.set_hls_color(0.33333,0.5,1.0)
    elif distance > 250:
        leds.set_hls_color(0.15,0.5,1.0)
    else:
        leds.set_hls_color(0.0,0.5,1.0)
    time.sleep(1)