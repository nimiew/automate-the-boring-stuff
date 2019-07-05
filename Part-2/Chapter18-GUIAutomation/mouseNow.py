#! python3
# mouseNow.py - Displays mouse cursor's current position

import pyautogui
print('Press CTRL-C to quit.')

try:
    while True: #keeps updating coords
        # Get and print mouse coords
        x, y = pyautogui.position()
        pos = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)

        print(pos, end='')
        print('\b' * len(pos), end='', flush=True) #erase old coords

except KeyboardInterrupt:
    print('\nDone.')
