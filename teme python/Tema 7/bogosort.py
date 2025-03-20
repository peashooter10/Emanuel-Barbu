import time
import random

def bogo_sort(data, drawData, timeTick):
    def is_sorted(data):
        for i in range(len(data)-1):
            if data[i]>data[i+1]:
                return False
        return True

    while not is_sorted(data):
        random.shuffle(data)
        drawData(data, ['red' for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, ['green' for x in range(len(data))])
    time.sleep(timeTick)
