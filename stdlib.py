import fileinput
import re
from collections import *  # noqa
from functools import partial, reduce  # noqa
from itertools import *  # noqa
from pprint import pformat, pprint  # noqa

from more_itertools import *  # noqa


class Flag:
    def __init__(self, flag: bool):
        self.flag = flag

    def true(self):
        self.flag = True

    def false(self):
        self.flag = False

    def __bool__(self):
        return self.flag


DEBUG = Flag(False)
EXAMPLE = Flag(False)


def ints(line):
    return [int(x) for x in re.findall(r"-?\d+", line)]


def read_input(filename=None):
    if filename is None:
        if EXAMPLE:
            filename = "example"
        else:
            filename = "input"

    return list(line.rstrip("\n") for line in fileinput.input(filename))


def identity(x):
    return x


def inverse_identity(x):
    return not x
