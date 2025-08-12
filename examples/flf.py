#! /usr/bin/env python3

from diagnosticism import (
    file,
    func,
    line,
    fileline,
    filelinefunc,
)

def f():

    print("  `file()`:", file())

    print("  `file(basename=True)`:", file(basename=True))

    print("  `line()`:", line())

    print("  `func()`:", func())

    print("  `fileline()`:", fileline())

    print("  `fileline(basename=True)`:", fileline(basename=True))

    print("  `filelinefunc()`:", filelinefunc())

    print("  `filelinefunc(basename=True)`:", filelinefunc(basename=True))


if __name__ == "__main__":

    print()
    print("in `f()`:")

    f()

    print()
    print("in `main()`:")

    print("  `file()`:", file())

    print("  `file(basename=True)`:", file(basename=True))

    print("  `line()`:", line())

    print("  `func()`:", func())

    print("  `fileline()`:", fileline())

    print("  `fileline(basename=True)`:", fileline(basename=True))

    print("  `filelinefunc()`:", filelinefunc())

    print("  `filelinefunc(basename=True)`:", filelinefunc(basename=True))

