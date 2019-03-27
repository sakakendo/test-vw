import atexit
import sys


def ret0():
    print("ret0")
    sys.exit(0)


atexit.register(ret0)
raise Exception
