#!/usr/bin/env python

import diagnosticism as d

import sys

def func1():

    #sys.stderr.write("locals(%s)=%s\n" % (type

    #d.trace()
    pass

def func2(x, y):

    d.trace()

def func3(x, y, **options):

    d.trace()

def func4(x, y, *args):

    d.trace()

def func5(x, y, *args, **options):

    d.trace()


d.enable_tracing(True)

func1()

func2('abc', 12)

func3('abc', 12)
func3('abc', 12, pos='left')

func4('abc', 12)
func4('abc', 12, 13, 14, 15)

func5('abc', 12)
func5('abc', 12, 13, 14, 15)
func5('abc', 12, pos='left', length='10')
func5('abc', 12, 13, 14, 15, pos='left', length='10')

