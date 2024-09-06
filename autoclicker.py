import keyboard
import mouse
import time


on = False


def set_clicker():
    global on
    if on == False:
        on = True
        print('Clicker: ON')
    else:
        on = False
        print('Clicker: OFF')


keyboard.add_hotkey('Alt + S', set_clicker)
while True:
    if on:
        mouse.double_click(button = 'left')
        time.sleep(0.001)
