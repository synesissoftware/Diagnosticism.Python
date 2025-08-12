#! /usr/bin/env python3

import asyncio
import diagnosticism as d

@d.asynctracefunc
async def func1():

    pass


@d.asynctracefunc
async def func2(x, y):

    pass


@d.asynctracefunc
async def func3(x, y, **options):

    z = x * y

    return z


@d.asynctracefunc
async def func4(x, y, *args):

    pass


@d.asynctracefunc
async def func5(x, y, *args, **options):

    pass


class Thing:


    @d.tracefunc
    def __init__(self):

        pass


    @d.asynctracefunc
    async def some_method(self, x, y, z):

        pass


@d.asynctracefunc
async def main():

    await asyncio.create_task(func1())

    await asyncio.create_task(func2('abc', 12))

    await asyncio.create_task(func3('abc', 12))
    await asyncio.create_task(func3('abc', 12, pos='left'))

    await asyncio.create_task(func4('abc', 12))
    await asyncio.create_task(func4('abc', 12, 13, 14, 15))

    await asyncio.create_task(func5('abc', 12))
    await asyncio.create_task(func5('abc', 12, 13, 14, 15))
    await asyncio.create_task(func5('abc', 12, pos='left', length=10))
    await asyncio.create_task(func5('abc', 12, 13, 14, 15, pos='left', length=10))

    thing = Thing()
    await asyncio.create_task(thing.some_method(-1, 0, +1))

    await asyncio.sleep(2.0)


d.enable_tracing(('DIAGNOSTICISM_ENABLE_TRACING', 'ENABLE_TRACING'), True)

asyncio.run(main())
