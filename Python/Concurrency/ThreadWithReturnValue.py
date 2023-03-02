import threading
import time


class ThreadWithReturnValue(threading.Thread):
    def run(self):
        self._return = None
        target = getattr(self, "_target")
        if target is not None:
            self._return = target(*getattr(self, "_args"), **getattr(self, "_kwargs"))

    def join_return(self):
        super().join()
        return self._return


def test(a, b, delay=0):
    time.sleep(delay)
    print(f"{threading.current_thread().name}: {a+b}")
    return a + b


if __name__ == "__main__":
    t = ThreadWithReturnValue(target=test, name="thread", args=(2, 3, 0))
    t1 = ThreadWithReturnValue(target=test, name="thread1", args=(6, 4, 2))
    #t = ThreadWithReturnValue(target=test, name="thread", kwargs={"a":2, "b":3, "delay":0})
    #t1 = ThreadWithReturnValue(target=test, name="thread1", args=(), kwargs={"a":6, "b":4, "delay":2})
    t.start()
    t1.start()
    print(t.join_return())
    print(t1.join_return())