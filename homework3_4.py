""" Multithreading example using event class """

import threading


def print_even(even_printed, odd_printed):
    """Print even number, set event variable for another thread and wait

    until odd printer sets event again
    """
    even_numbers = iter(range(0, 101, 2))
    try:
        while True:
            odd_printed.clear()
            print(next(even_numbers))
            even_printed.set()
            odd_printed.wait()
    except StopIteration:
        return


def print_odd(even_printed, odd_printed):
    """Reset an event variable for another thread, print an odd number and throw

    a signal to even printer, then wait its signal
    """
    odd_numbers = iter(range(1, 100, 2))
    try:
        while True:
            if even_printed.is_set():
                even_printed.clear()
                print(next(odd_numbers))
                odd_printed.set()
    except StopIteration:
        odd_printed.set()
        return


if __name__ == '__main__':
    ev_1 = threading.Event()
    ev_2 = threading.Event()

    even_printer = threading.Thread(name='even',
                                    target=print_even,
                                    args=(ev_1, ev_2,))
    odd_printer = threading.Thread(name='odd',
                                   target=print_odd,
                                   args=(ev_1, ev_2))
    even_printer.start()
    odd_printer.start()
