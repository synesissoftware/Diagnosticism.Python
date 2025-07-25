# ######################################################################## #
# File:     doomgram.py
#
# Purpose:  Definition of the `DOOMGram` class.
#
# Created:  19th July 2025
# Updated:  24th July 2025
#
# Author:   Matthew Wilson
#
# Copyright (c) 2025, Matthew Wilson and Synesis Information Systems
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# ######################################################################## #


import math
import time


class DOOMGram:
    """
    Decimal Order-Of-Magnitude frequency histoGRAM.
    """

    __slots__ = (

        '_event_count',
        '_total_event_time_ns',
        '_min_event_time_ns',
        '_max_event_time_ns',
        '_num_events_in_1ns',
        '_num_events_in_10ns',
        '_num_events_in_100ns',
        '_num_events_in_1us',
        '_num_events_in_10us',
        '_num_events_in_100us',
        '_num_events_in_1ms',
        '_num_events_in_10ms',
        '_num_events_in_100ms',
        '_num_events_in_1s',
        '_num_events_in_10s',
        '_num_events_ge_100s',
    )

    def __init__(self):

        self._event_count           =   0

        self._total_event_time_ns   =   0

        self._min_event_time_ns     =   None
        self._max_event_time_ns     =   None

        self._num_events_in_1ns     =   0
        self._num_events_in_10ns    =   0
        self._num_events_in_100ns   =   0
        self._num_events_in_1us     =   0
        self._num_events_in_10us    =   0
        self._num_events_in_100us   =   0
        self._num_events_in_1ms     =   0
        self._num_events_in_10ms    =   0
        self._num_events_in_100ms   =   0
        self._num_events_in_1s      =   0
        self._num_events_in_10s     =   0
        self._num_events_ge_100s    =   0

    def event_count(self):
        """
        Number of events counted.
        """

        return self._event_count

    def total_event_time_ns(self):
        """
        Obtains the total event time (in nanoseconds).
        """

        return self._total_event_time_ns

    def min_event_time_ns(self):
        """
        Obtain the minimum event time (in nanoseconds), or +None+ if no
        events.
        """

        return self._min_event_time_ns

    def max_event_time_ns(self):
        """
        Obtain the maximum event time (in nanoseconds), or +None+ if no
        events.
        """

        return self._max_event_time_ns

    def num_events_in_1ns(self):
        """
        Number of events counted in the interval [1ns, 10ns).
        """

        return self._num_events_in_1ns

    def num_events_in_10ns(self):
        """
        Number of events counted in the interval [10ns, 100ns).
        """

        return self._num_events_in_10ns

    def num_events_in_100ns(self):
        """
        Number of events counted in the interval [100ns, 1µs).
        """

        return self._num_events_in_100ns

    def num_events_in_1us(self):
        """
        Number of events counted in the interval [1µs, 10µs).
        """

        return self._num_events_in_1us

    def num_events_in_10us(self):
        """
        Number of events counted in the interval [10µs, 100µs).
        """

        return self._num_events_in_10us

    def num_events_in_100us(self):
        """
        Number of events counted in the interval [100µs, 1ms).
        """

        return self._num_events_in_100us

    def num_events_in_1ms(self):
        """
        Number of events counted in the interval [1ms, 10ms).
        """

        return self._num_events_in_1ms

    def num_events_in_10ms(self):
        """
        Number of events counted in the interval [10ms, 100ms).
        """

        return self._num_events_in_10ms

    def num_events_in_100ms(self):
        """
        Number of events counted in the interval [100ms, 1s).
        """

        return self._num_events_in_100ms

    def num_events_in_1s(self):
        """
        Number of events counted in the interval [1s, 10s).
        """

        return self._num_events_in_1s

    def num_events_in_10s(self):
        """
        Number of events counted in the interval [10s, 100s).
        """

        return self._num_events_in_10s

    def num_events_ge_100s(self):
        """
        Number of events counted in the interval [100s, ∞).
        """

        return self._num_events_ge_100s

    def push_event_time_ns(self, time_in_ns):
        """
        Pushes an event with the given number of nanoseconds.
        """

        assert isinstance(time_in_ns, int)

        self._event_count += 1

        self._total_event_time_ns += time_in_ns


        if self._min_event_time_ns is None or time_in_ns < self._min_event_time_ns:

            self._min_event_time_ns = time_in_ns


        if self._max_event_time_ns is None or self._max_event_time_ns < time_in_ns:

            self._max_event_time_ns = time_in_ns



        if time_in_ns >= 100_000_000:

            if time_in_ns >= 10_000_000_000:

                if time_in_ns >= 100_000_000_000:

                    self._num_events_ge_100s += 1
                else:

                    self._num_events_in_10s += 1

            else:

                if time_in_ns >= 1_000_000_000:

                    self._num_events_in_1s += 1
                else:

                    self._num_events_in_100ms += 1

        else:

            if time_in_ns >= 10_000:

                if time_in_ns >= 1_000_000:

                    if time_in_ns >= 10_000_000:

                        self._num_events_in_10ms += 1
                    else:

                        self._num_events_in_1ms += 1

                else:

                    if time_in_ns >= 100_000:

                        self._num_events_in_100us += 1
                    else:

                        self._num_events_in_10us += 1
            else:

                if time_in_ns >= 100:

                    if time_in_ns >= 1_000:

                        self._num_events_in_1us += 1
                    else:

                        self._num_events_in_100ns += 1
                else:

                    if time_in_ns >= 10:

                        self._num_events_in_10ns += 1
                    elif time_in_ns >= 1:

                        self._num_events_in_1ns += 1

    def push_event_time_us(self, time_in_us):
        """
        Pushes an event with the given number of microseconds.
        """

        self.push_event_time_ns(time_in_us * 1_000)

    def push_event_time_ms(self, time_in_ms):
        """
        Pushes an event with the given number of milliseconds.
        """

        self.push_event_time_ns(time_in_ms * 1_000_000)

    def push_event_time_s(self, time_in_s):
        """
        Pushes an event with the given number of seconds.
        """

        self.push_event_time_ns(time_in_s * 1_000_000_000)

    def to_strip(self, **kwargs):
        """
        Converts to string form according to given options

        === Signature

        * *Parameters:*
          - +options+ (+Hash+, +Integer+) Combination of flags (with behaviour as described below for the +flags+ option), or an options hash;

        * *Options:*
          - +overflow_character+ (+String+) A string (of length 1) that specifies the symbol for counts outside the available range. Defaults to +'*'+;
          - +range+ (+String+) A string whose characters specificy the symbols to use for counts in orders of magnitude. Defaults to +'abcdefghijklmnopqrstuvwxyz'+, which caters to the counts 1-9 => +'a', 10-99 => +'b'+, 100-999 => +'c'+, ... 10^25-(10^26-1) => +'z'+;
          - +zero_character+ (+String+) A string (of length 1) that specifies the symbol for a count of 0. Defaults to +' '+;

        === Return
        (+String+) A string (of length 12) containing symbols representing the counts in the ranges 1ns, 10ns, ..., 10s, 100+s.
        """

        ch_zero     =   kwargs.get('zero', '_')
        ch_overflow =   kwargs.get('overflow', '*')
        range_chars =   kwargs.get('range', 'abcdefghijklmnopqrstuvwxyz')

        counts = [
            self._num_events_in_1ns,
            self._num_events_in_10ns,
            self._num_events_in_100ns,
            self._num_events_in_1us,
            self._num_events_in_10us,
            self._num_events_in_100us,
            self._num_events_in_1ms,
            self._num_events_in_10ms,
            self._num_events_in_100ms,
            self._num_events_in_1s,
            self._num_events_in_10s,
            self._num_events_ge_100s,
        ]

        s = [ch_zero[0]] * 12 # "____________"

        for index, count in enumerate(counts):

            if 0 == count:

                continue

            # TODO: get a faster way to count digits

            oom = int(math.log10(count))

            if oom < len(range_chars):

                s[index] = range_chars[oom]
            else:

                s[index] = ch_overflow[0]

        return ''.join(s)

    def __repr__(self):
        """
        A representation of the `DOOMGram` instance that shows all internal
        state.
        """

        return "%s(%s=%d, %s=%d, %s=%s, %s=%s, %s=%d, %s=%d, %s=%d, %s=%d, %s=%d, %s=%d, %s=%d, %s=%d, %s=%d, %s=%d, %s=%d, %s=%d)" % (
            'DOOMGram',
            'event_count',          self.event_count(),
            'total_event_time_ns',  self.total_event_time_ns(),
            'min_event_time_ns',    self.min_event_time_ns(),
            'max_event_time_ns',    self.max_event_time_ns(),
            'num_events_in_1ns',    self.num_events_in_1ns(),
            'num_events_in_10ns',   self.num_events_in_10ns(),
            'num_events_in_100ns',  self.num_events_in_100ns(),
            'num_events_in_1us',    self.num_events_in_1us(),
            'num_events_in_10us',   self.num_events_in_10us(),
            'num_events_in_100us',  self.num_events_in_100us(),
            'num_events_in_1ms',    self.num_events_in_1ms(),
            'num_events_in_10ms',   self.num_events_in_10ms(),
            'num_events_in_100ms',  self.num_events_in_100ms(),
            'num_events_in_1s',     self.num_events_in_1s(),
            'num_events_in_10s',    self.num_events_in_10s(),
            'num_events_ge_100s',   self.num_events_ge_100s(),
        )

    def __str__(self):
        """
        Converts to string form according to default options.
        """

        return self.to_strip()


class DOOMScope:
    """
    Scoping class for histogram timings using `DOOMScope`.
    """

    __slots__ = (
        '_dg',
        '_before',
    )

    def __init__(self, dg):

        assert isinstance(dg, DOOMGram)

        self._dg = dg
        self._before = None

    def __enter__(self):

        self._before = time.perf_counter_ns()

        return self._dg

    def __exit__(self, x_type, x_val, x_tb):

        after = time.perf_counter_ns()

        self._dg.push_event_time_ns(after - self._before)


# ############################## end of file ############################# #

