#!/usr/bin/env python

import diagnosticism as d
import diagnosticism.severity as sev

d.enable_logging(True)

d.log(sev.TRACE, 'trace')
d.log(sev.INFO, 'info')
d.log(sev.DEBUG2, 'debug2')
d.log(sev.ALERT, "and we're out")

