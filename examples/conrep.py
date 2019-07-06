#!/usr/bin/env python

import diagnosticism as d

d.set_program_name('ConRep')

d.conrep('some important information')
d.conrep("some slightly less important information: %s, %d, %f" % ('abc', -1, 234.567), show_program_name=False)

d.abort("and we're out")
d.conrep("ERROR: should not get here!")

