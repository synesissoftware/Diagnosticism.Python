#! /usr/bin/env python3

import diagnosticism as d

@d.tracefunc
def func1():

    pass


@d.tracefunc
def func2(x, y):

    pass


@d.tracefunc
def func3(x, y, **options):

    z = x * y

    return z


@d.tracefunc
def func4(x, y, *args):

    pass


@d.tracefunc
def func5(x, y, *args, **options):

    pass


class Thing:


    @d.tracefunc
    def __init__(self):

        pass


    @d.tracefunc
    def some_method(self, x, y, z):

        pass


d.enable_tracing(('DIAGNOSTICISM_ENABLE_TRACING', 'ENABLE_TRACING'), True)


func1()

func2('abc', 12)

func3('abc', 12)
func3('abc', 12, pos='left')

func4('abc', 12)
func4('abc', 12, 13, 14, 15)

func5('abc', 12)
func5('abc', 12, 13, 14, 15)
func5('abc', 12, pos='left', length=10)
func5('abc', 12, 13, 14, 15, pos='left', length=10)

thing = Thing()
thing.some_method(-1, 0, +1)

