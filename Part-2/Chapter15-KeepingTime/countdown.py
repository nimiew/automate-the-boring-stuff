#! python3
# countdown.py

import time, subprocess, sys

if len(sys.argv)==2:
    try:
        timeLeft = int(sys.argv[1])
    except ValueError:
        print('Not an integer. Program will close.')
        print('Usage: countdown.py <int>')
        sys.exit()
elif len(sys.argv)<2:
    while True:
        try:
            timeLeft = int(input('Countdown timer. Enter number of seconds: e.g. 5\n'))
            break
        except ValueError:
            print('Not an integer.')
else:
    print('Not an integer. Program will close.')
    print('Usage: countdown.py <int>')
    sys.exit()

try:
    print('Beginning countdown...')
    while timeLeft > 0:
        print('Time Left: %d' % timeLeft)
        time.sleep(1)
        timeLeft-=1

    subprocess.Popen(['start', 'alarm.wav'], shell=True)

except KeyboardInterrupt:
    print('Countdown cancelled.')


