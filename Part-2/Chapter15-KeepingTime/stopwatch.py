#! python3
# stopwatch.py - Stopwatch

import time

print('Press ENTER to begin. Press ENTER subsequently to count laps.\n')
print('Press CTRL-C to quit.\n')

input()
print('Started.\n')

startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        timeElapsed = round(time.time() - startTime, 2)
        print('Lap #%d: %s (%s)' % (lapNum, timeElapsed, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # reset last lap time
except KeyboardInterrupt:
    print('\nDone.')
