#! /usr/bin/env python3
"""
Manual timings for logging and DOOMGram updates.

unittest discover does not collect this file. Run it directly:

    PYTHONPATH=. python3 tests/performance/bench_logging.py
"""

from diagnosticism.doomgram import DOOMGram
from diagnosticism.logging import (
    enable_logging,
    log,
)
from diagnosticism.severity import INFORMATIONAL

import time


_REPEATS = 10000


def _elapsed(action):

    started = time.perf_counter()

    action()

    return time.perf_counter() - started


def _disabled_log():

    enable_logging(False)

    for _ in range(_REPEATS):

        log(INFORMATIONAL, "bench")


class _Discard(object):

    def isatty(self):

        return False

    def write(self, text):

        return len(text)


def _enabled_log():

    enable_logging(True)

    sink = _Discard()

    for _ in range(_REPEATS):

        log(INFORMATIONAL, "bench", file=sink)


def _doomgram_updates():

    gram = DOOMGram()

    for index in range(_REPEATS):

        gram.push_event_time_ns(index + 1)


def main():

    print("disabled log: %.6fs" % _elapsed(_disabled_log))
    print("enabled log:  %.6fs" % _elapsed(_enabled_log))
    print("DOOMGram:     %.6fs" % _elapsed(_doomgram_updates))


if __name__ == '__main__':

    main()
