""" Multithreading example using timer object """

from threading import Timer
import time


def print_num(numbers):
    """Print a number from a range and wait for 1 second"""
    for i in numbers:
        print(i)
        time.sleep(1)


if __name__ == '__main__':
    thread_1 = Timer(interval=2, function=print_num, args=[range(0, 101, 2)])
    thread_2 = Timer(interval=2.5, function=print_num, args=[range(1, 100, 2)])
    thread_1.start()
    thread_2.start()
