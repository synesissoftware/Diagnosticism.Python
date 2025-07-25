#! /usr/bin/env python3

import diagnosticism as d


d.enable_logging(False)

d.warn("I warned you!")


d.enable_logging(True)

d.warn("I warned you!")

