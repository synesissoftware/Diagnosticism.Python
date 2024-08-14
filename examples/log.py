#! /usr/bin/env python3

import diagnosticism as d
import diagnosticism.severity as sev

d.enable_logging(True)

d.set_log_filter(sev.INFO)

d.log(sev.TRACE, 'trace')
d.log(sev.INFO, 'info')
d.log(sev.DEBUG2, 'debug2')
d.log(sev.ALERT, "and we're out")

