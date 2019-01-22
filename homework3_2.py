""" Multithreading example using condition variable """

import threading


def print_number(condition_var, numbers, limit):
    """Print a number from a range and wait until a signal

     received from another thread"""

    with condition_var:
        for i in numbers:
            print(i)
            condition_var.notifyAll()
            if i == limit:
                break
            else:
                condition_var.wait()


if __name__ == '__main__':
    condition = threading.Condition()
    thread_1 = threading.Thread(target=print_number,
                                args=(condition, range(0, 101, 2), 100))
    thread_2 = threading.Thread(target=print_number,
                                args=(condition, range(1, 100, 2), 100))

    thread_1.start()
    thread_2.start()
