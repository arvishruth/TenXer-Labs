from gpiozero import PWMLED
from time import sleep


from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)

button.when_pressed = led.on
button.when_released = led.off



led1 = PWMLED(27)

while True:
    led1.value = 0  # off
    sleep(0.5)
    led1.value = 0.1  # off
    sleep(0.5)
    led1.value = 0.2  # off
    sleep(0.5)
    led1.value = 0.3  # off
    sleep(0.5)
    led1.value = 0.4  # off
    sleep(0.5)
    led1.value = 0.5  # half brightness
    sleep(0.5)
    led1.value = 0.6  # off
    sleep(0.5)
    led1.value = 0.7  # off
    sleep(0.5)
    led1.value = 0.8  # off
    sleep(0.5)
    led1.value = 0.9  # off
    sleep(0.5)
    led1.value = 1  # full brightness
    sleep(0.5)