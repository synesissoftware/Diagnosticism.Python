# -*- coding: utf-8 -*-

# ######################################################################## #
# File:     time_format/nanoseconds.py
#
# Purpose:  Nanosecond duration formatting.
#
# Created:  24th August 2025
# Updated:  27th June 2026
#
# Copyright (c) 2026-2027, Matthew Wilson and Synesis Information Systems
# All rights reserved.
#
# ######################################################################## #


from . import (
    _fmt,
    _scale_index,
    _SUFFIXES,
)

# NOTE: this work was brought in from **asynkio** at version 0.16

def nanoseconds_to_string(nanoseconds, format_spec=''):
    """
    Formats a nanosecond count as a compact human-readable duration string.

    The output adapts the unit (``ns``, ``µs``, ``ms``, ``s``) and decimal
    precision to keep roughly three significant digits in the numeric
    portion.

    Parameters
    ----------
    nanoseconds : int
        The duration, in nanoseconds.
    format_spec : str, optional
        Formatting options. The only recognised flag is ``+``, which causes
        positive values to include an explicit leading sign. Other
        characters are ignored.

    Returns
    -------
    str
        The formatted duration string. Zero is always ``"0s"`` with no sign.
    """

    v = int(nanoseconds)

    if v < 0:
        v = -v
        sign = '-'
    else:
        if '+' in format_spec:
            sign = '+'
        else:
            sign = ''

    if v == 0:
        return "0s"

    oom, divisor = _scale_index(v)

    suffix = _SUFFIXES[oom // 3]

    if oom < 3:
        return _fmt(sign, v, 0, suffix)

    divisor_0 = divisor // 1000  # 1,000

    i = oom % 3

    if i == 0:
        divisor_1 = 1000  # 1,000
    elif i == 1:
        divisor_1 = 100
    else:
        divisor_1 = 10

    v //= divisor_0

    whole = v // divisor_1
    frac = v - (whole * divisor_1)

    return _fmt(
        sign,
        whole,
        frac,
        suffix,
    )


# ############################## end of file ############################# #
