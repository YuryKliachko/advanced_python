""" Multithreading example using condition variable """
import multiprocessing


def print_number(condition_var, numbers, limit):
    """Print a number from a range (even or odd), then notify another process and wait

    until it sends a signal
    """

    with condition_var:
        for i in numbers:
            print(i)
            condition_var.notify_all()
            if i == limit:
                break
            else:
                condition_var.wait()


if __name__ == '__main__':
    condition = multiprocessing.Condition()
    process_1 = multiprocessing.Process(target=print_number,
                                        args=(condition, range(0, 101, 2), 100))
    process_2 = multiprocessing.Process(target=print_number,
                                        args=(condition, range(1, 100, 2), 10))

    process_1.start()
    process_2.start()
