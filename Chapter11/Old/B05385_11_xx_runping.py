import subprocess
import time

proc = subprocess.Popen(
    ["ping", "-c", "10", "localhost"],
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    stderr=subprocess.PIPE)

counter = 0
for line in iter(proc.stdout.readline, ''):
    print line
    progress.setPercentage( counter )
    counter +=10


