# -*- coding: utf-8 -*-

# ######################################################################## #
# File:     time_format/__init__.py
#
# Purpose:  Time formatting utilities.
#
# Created:  24th August 2025
# Updated:  27th June 2026
#
# Author:   Matthew Wilson
#
# Copyright (c) 2025-2026, Matthew Wilson and Synesis Information Systems
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


import sys

if sys.version_info[0] >= 3:
    from ._fmt_py3 import _fmt
else:
    from ._fmt_py2 import _fmt


_SCALES = (
    1,
    10,
    100,
    1000,  # 1,000
    10000,  # 10,000
    100000,  # 100,000
    1000000,  # 1,000,000
    10000000,  # 10,000,000
    100000000,  # 100,000,000
    1000000000,  # 1,000,000,000
    10000000000,  # 10,000,000,000
    100000000000,  # 100,000,000,000
)

_SUFFIXES = (
    'ns',
    'µs',
    'ms',
    's',
)


def _scale_index(n):
    """
    Selects an order-of-magnitude band for the given positive nanosecond
    count.
    """

    assert n > 0
    assert len(_SCALES) == 12

    if n >= 100000000000:  # 100,000,000,000

        return (11, _SCALES[11])

    l = 0
    h = 11

    count = 0

    while l <= h:
        count += 1

        assert count < 5, "too many loops while trying to scale %s" % n

        m = (h + l) // 2

        b = _SCALES[m]

        if n == b:
            return (m, b)

        if n < b:
            h = m

            continue

        assert n > b

        if n < b * 10:
            return (m, b)

        l = m

    return (11, _SCALES[11])


from .nanoseconds import nanoseconds_to_string


# ############################## end of file ############################# #
