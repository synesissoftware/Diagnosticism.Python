#! /usr/bin/env python3

import diagnosticism as d
import diagnosticism.severity as sev

import os


ENV_VAR_NAME = 'DP_LOG_THRESHOLD'
FILTER_LEVEL = sev.INFO


d.enable_logging(('DIAGNOSTICISM_ENABLE_LOGGING', 'ENABLE_LOGGING'), True)


if ENV_VAR_NAME in os.environ:

    try:

        threshold = int(os.environ[ENV_VAR_NAME])

        d.set_log_filter(threshold)
    except ValueError:

        d.abort("environment variable '%s' exists and has a value not convertible to `int`" % (ENV_VAR_NAME))
else:

    d.set_log_filter(FILTER_LEVEL)

d.log(sev.BENCHMARK, 'benchmark')
d.log(sev.TRACE, 'trace')
d.log(sev.DEBUG5, 'debug5')
d.log(sev.DEBUG4, 'debug4')
d.log(sev.DEBUG3, 'debug3')
d.log(sev.DEBUG2, 'debug2')
d.log(sev.DEBUG1, 'debug1')
d.log(sev.DEBUG0, 'debug0')
d.log(sev.INFO, 'informational')
d.log(sev.NOTICE, 'notice')
d.log(sev.WARNING, 'warning')
d.log(sev.FAILURE, 'failure')
d.log(sev.CRITICAL, 'critical')
d.log(sev.ALERT, "alert")
d.log(sev.VIOLATION, "VIOLATION")

