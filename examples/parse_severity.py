#! /usr/bin/env python

from diagnosticism.contingent_reporting import abort (
    d_abort,
    get_program_name,
    parse_verbosity,
)

import sys


if len(sys.argv) != 2:

    d_abort("wrong number of arguments", trailing_prompt=True)
else:

    if '--help' == sys.argv[1]:

        print("USAGE: %s <severity-name-or-value>" % (get_program_name()))

        sys.exit(0)
    else:

        severity_string = sys.argv[1]


try:

    severity = parse_verbosity(severity_string)

    print("given severity string '%s' is parsed as %d" % (severity_string, severity))
    # d_abort(

except ValueError as x:

    print("exception (%s): %s" % (type(x), str(x)), file=sys.stderr, flush=True)


