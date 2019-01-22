""" Multithreading example using semaphores """

from threading import Thread, Semaphore
import time

shared_num = []


def print_even(even_sem, odd_sem, _limit):
    """Acquire a semaphore and print an even number, then release a semaphore
     for an opposite thread"""
    for i in range(0, limit + 1, 2):
        even_sem.acquire()
        print(i)
        shared_num.append(i + 1)
        if i >= _limit:
            break
        odd_sem.release()
    odd_sem.release()


def print_odd(even_sem, odd_sem, _limit):
    """Acquire a semaphore and print an odd number, then release a semaphore
     for an opposite thread"""
    while True:
        odd_sem.acquire()
        if not shared_num:
            break
        odd = shared_num.pop()
        if odd > _limit:
            break
        print(odd)
        even_sem.release()


if __name__ == '__main__':
    sem_1 = Semaphore(1)
    sem_2 = Semaphore(0)

    limit = 100

    thread_1 = Thread(target=print_even, args=(sem_1, sem_2, limit))
    thread_2 = Thread(target=print_odd, args=(sem_1, sem_2, limit))

    thread_1.start()
    time.sleep(2)
    thread_2.start()
