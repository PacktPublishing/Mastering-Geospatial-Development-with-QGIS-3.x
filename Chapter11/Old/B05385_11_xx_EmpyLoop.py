import time
for index in range(100):
    progress.setPercentage(index)
    print index
    time.sleep(0.1)
