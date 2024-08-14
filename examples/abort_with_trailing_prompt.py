#! /usr/bin/env python3

import diagnosticism as d

d.set_program_name('ConRep')

d.abort("abort with application-defined TRAILING_PROMPT", trailing_prompt='use --help for help', do_exit=False)

d.abort("default abort", do_exit=False)

d.abort("default abort with default TRAILING_PROMPT", do_exit=False, trailing_prompt=True)

print("setting default trailing prompt")
d.contingent_reporting.set_default_trailing_prompt('use --help to show usage')

d.abort("default abort with default TRAILING_PROMPT", do_exit=False, trailing_prompt=True)

d.abort("default abort", do_exit=False)


