""" Make a segfault by exceeding recursion limit """
import sys


def recursive(arg):
    """ Get a recursion limit and increase it to cause a sagfault """
    print(arg)
    sys.setrecursionlimit(sys.getrecursionlimit() + 1)
    recursive(arg + 1)


if __name__ == '__main__':
    recursive(1)
