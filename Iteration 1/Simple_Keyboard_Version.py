import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

rows = [board.GP2, board.GP3, board.GP4, board.GP5]
cols = [board.GP6, board.GP7, board.GP8, board.GP9]

row_pins = []
col_pins = []

# Setup rows (output)
for r in rows:
    pin = digitalio.DigitalInOut(r)
    pin.direction = digitalio.Direction.OUTPUT
    pin.value = True
    row_pins.append(pin)

# Setup columns (input pull-up)
for c in cols:
    pin = digitalio.DigitalInOut(c)
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP
    col_pins.append(pin)

#  Key mapping (customize this!)
keys = [
    [Keycode.ESCAPE, Keycode.ONE, Keycode.TWO, Keycode.THREE],
    [Keycode.FOUR, Keycode.FIVE, Keycode.SIX, Keycode.SEVEN],
    [Keycode.EIGHT, Keycode.NINE, Keycode.ZERO, Keycode.ENTER],
    [Keycode.SPACE, Keycode.LEFT_ARROW, Keycode.RIGHT_ARROW, Keycode.UP_ARROW]
]

pressed = set()

while True:
    for i, row in enumerate(row_pins):
        row.value = False

        for j, col in enumerate(col_pins):
            key = keys[i][j]

            if not col.value:  # pressed
                if key not in pressed:
                    kbd.press(key)
                    pressed.add(key)
            else:
                if key in pressed:
                    kbd.release(key)
                    pressed.remove(key)

        row.value = True

    time.sleep(0.02)
