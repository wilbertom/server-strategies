import queue
import threading

class ThreadPool:

    def __init__(self, threads, work):
        self._queue = queue.Queue()
        self._threads = []
        self._work = work
        self._stop = False

        for i in range(threads):
            thread = threading.Thread(target=self._run)
            thread.start()
            self._threads.append(thread)

    def put(self, item):
        self._queue.put(item, block=False)

    def stop(self):
        self._stop = True

    def _run(self):
        while True:
            if self._stop:
                break

            try:
                item = self._queue.get(block=True, timeout=3)
                self._work(item)
            except queue.Empty:
                pass

