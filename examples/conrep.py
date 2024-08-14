#! /usr/bin/env python3

import diagnosticism as d

d.set_program_name('ConRep')

d.report('some important information')
d.report("some slightly less important information: %s, %d, %f" % ('abc', -1, 234.567), show_program_name=False)

d.abort("and we're out")
d.report("ERROR: should not get here!")


