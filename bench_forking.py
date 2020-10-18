from datetime import datetime
import os
import sys


forks = int(sys.argv[1])

start = datetime.utcnow()

for i in range(forks):
    pid = os.fork()

    if pid == 0:
        sys.exit(0)

end = datetime.utcnow()

time = (end - start).seconds

print(f"{time} seconds, {forks / time} forks per second")

try:
    while True:
        os.wait()
except ChildProcessError:
    pass
