#! /usr/bin/env python3

from diagnosticism import (
    DOOMGram,
    DOOMScope,
)

import random
import time


def main():

    dg = DOOMGram()

    for _ in range(1000):

        r = random.uniform(1, 1000)

        d = r / 1_000_000

        with DOOMScope(dg):

            time.sleep(d)

    print("dg:", dg)


if __name__ == "__main__":

    main()
