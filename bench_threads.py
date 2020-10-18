from datetime import datetime
import sys
import threading

def target():
    sys.exit(0)

threads = int(sys.argv[1])

start = datetime.utcnow()

for i in range(threads):
    threading.Thread(target=target).start()

end = datetime.utcnow()

time = (end - start).seconds

print(f"{time} seconds, {threads / time} threads per second")

for thread in threading.enumerate():

    if thread != threading.current_thread():
        thread.join()
