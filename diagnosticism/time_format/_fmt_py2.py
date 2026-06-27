# -*- coding: utf-8 -*-

# ######################################################################## #
# File:     time_format/_fmt_py2.py
#
# Purpose:  Python 2.7 implementation of `_fmt()`.
#
# Created:  24th August 2025
# Updated:  27th June 2026
#
# Copyright (c) 2026-2027, Matthew Wilson and Synesis Information Systems
# All rights reserved.
#
# ######################################################################## #


def _fmt(
    sign,
    whole,
    frac,
    suffix,
):
    """
    Formats whole and fractional parts into a compact duration string.
    """

    if frac == 0:
        return "%s%s%s" % (sign, whole, suffix)

    if whole > 999:
        return "%s%s%s" % (sign, whole, suffix)

    if whole > 99:
        return "%s%s.%s%s" % (sign, whole, frac, suffix)

    if whole > 9:
        return "%s%s.%02d%s" % (sign, whole, frac, suffix)

    return "%s%s.%s%s" % (sign, whole, frac, suffix)


# ############################## end of file ############################# #
