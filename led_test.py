from gpiozero import LED
from time import sleep

green4 = LED(4)
green3 = LED(17)
green2 = LED(27)
green1 = LED(22)

blue = LED(12)

red1 = LED(16)
red2 = LED(13)
red3 = LED(19)
red4 = LED(26)


def test(name, led):
    print('Testing', name)
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)


test('green4', green4)
test('green3', green3)
test('green2', green2)
test('green1', green1)

test('blue', blue)

test('red1', red1)
test('red2', red2)
test('red3', red3)
test('red4', red4)

