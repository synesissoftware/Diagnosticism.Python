#! /usr/bin/env python3

from diagnosticism import (
    dbg,
    dbgfl,
    enable_tracing,
)

import sys


def f():

    print("about to call dbg on an int and a string")

    dbg()
    dbg(10)
    dbg(10, 20)
    dbg(i=10)
    dbg(i=10, j='abc')

    dbg('s', 't')


    dbgfl()
    dbgfl(10)
    dbgfl(10, 20)
    dbgfl(i=10)
    dbgfl(i=10, j='abc')

    dbgfl('s', 't')


if __name__ == "__main__":

    enable_tracing(True)

    print("")
    print("`main()`:")

    print("about to call dbg on an int and a string")

    dbg()
    dbg(10)
    dbg(10, 20)
    dbg(i=10)
    dbg(i=10, j='abc')

    dbg('s')
    dbg('s', 't')


    dbgfl()
    dbgfl(10)
    dbgfl(10, 20)
    dbgfl(i=10)
    dbgfl(i=10, j='abc')

    dbgfl('s', 't')



    print("")
    print("`f()`:")

    f()

