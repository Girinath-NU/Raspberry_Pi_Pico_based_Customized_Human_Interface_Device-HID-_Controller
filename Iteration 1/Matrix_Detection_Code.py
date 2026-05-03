import time
import board
import digitalio

pins = [
    board.GP2, board.GP3, board.GP4, board.GP5,
    board.GP6, board.GP7, board.GP8, board.GP9
]

pin_objs = []

for p in pins:
    pin = digitalio.DigitalInOut(p)
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP
    pin_objs.append(pin)

while True:
    for i in range(len(pin_objs)):
        for j in range(len(pin_objs)):
            if i != j:
                # set one as output low
                pin_objs[i].direction = digitalio.Direction.OUTPUT
                pin_objs[i].value = False

                pin_objs[j].direction = digitalio.Direction.INPUT
                pin_objs[j].pull = digitalio.Pull.UP

                if not pin_objs[j].value:
                    print("Connection:", i, j)

                # reset
                pin_objs[i].direction = digitalio.Direction.INPUT

    time.sleep(0.2)
