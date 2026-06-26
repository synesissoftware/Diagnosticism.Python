#! /usr/bin/env python3

# NOTE: This example requires Python 3+ (uses DOOMScope / perf_counter_ns and
# PEP 515 numeric literals).

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
