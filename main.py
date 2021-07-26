# Importing nessecary libraries.
import time
from machine import Pin
from machine import ADC

# Initializing object to use with connected sensors
adc = ADC()

# Setting up temp meter with the correct pin
apinTemp = adc.channel(pin='P16')

# Setting up the light meter with the correct pin
LightSensorPin = 'P13'
lightPin = Pin(LightSensorPin, mode=Pin.IN)
apinLight = adc.channel(attn=ADC.ATTN_11DB, pin=LightSensorPin)

# Do until all time
while True:
    # Calculating temp based on volts
    millivolts = apinTemp.voltage()
    celsius = (millivolts - 500.0) / 10.0

    # Sends a signal to Pybytes which will store their database as well as show up in the dashboard
    pybytes.send_signal(2, celsius)
    print("sending: {}".format(celsius))

    # Reads current light value
    val = apinLight()

    # Sends a signal to Pybytes which will store their database as well as show up in the dashboard
    pybytes.send_signal(1, val)
    print("Value", val)

    # Wait 30 minutes
    time.sleep(1800)
