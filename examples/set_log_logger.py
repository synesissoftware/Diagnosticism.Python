#! /usr/bin/env python3

import diagnosticism as d
import diagnosticism.severity as sev

import logging
import sys


logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s %(name)s: %(message)s',
    stream=sys.stdout,
)

d.enable_logging(True)
d.set_log_logger(logging.getLogger('app'))

d.log(sev.FAILURE, 'failure-text')
d.log(sev.WARNING, 'warning-text')
d.log(sev.INFO, 'info-text')
d.log(sev.DEBUG2, 'debug-text')

d.warn('warn-text')

d.log(sev.WARNING, 'still-on-stderr', file=sys.stderr)

d.set_log_logger(None)

d.log(sev.INFO, 'back-on-stderr')
