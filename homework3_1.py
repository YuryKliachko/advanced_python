""" Multithreading example using lock """
from threading import Thread, Lock
import time


def print_using_lock(nums, lock):
    """ Each threads acquires lock and prints the next number from its range"""
    try:
        while True:
            lock.acquire()
            print(next(nums))
            lock.release()
            time.sleep(0.1)
    except StopIteration:
        lock.release()
        return


if __name__ == '__main__':

    _lock = Lock()
    thread_1 = Thread(target=print_using_lock, args=(iter(range(0, 101, 2)), _lock, ))
    thread_2 = Thread(target=print_using_lock, args=(iter(range(1, 100, 2)), _lock, ))
    thread_1.start()
    time.sleep(0.05)
    thread_2.start()
