import time
from machine import Pin
from machine import ADC

adc = ADC()

apinTemp = adc.channel(pin='P16')

LightSensorPin = 'P13'
lightPin = Pin(LightSensorPin, mode=Pin.IN)
apinLight = adc.channel(attn=ADC.ATTN_11DB, pin=LightSensorPin)


while True:
    millivolts = apinTemp.voltage()
    celsius = (millivolts - 500.0) / 10.0

    pybytes.send_signal(2, celsius)
    print("sending: {}".format(celsius))

    val = apinLight()
    print("Value", val)

    time.sleep(5)
