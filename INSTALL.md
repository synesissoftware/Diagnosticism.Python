# Diagnosticism.Python - Installation and Use <!-- omit in toc -->


## Table of Contents <!-- omit in toc -->

- [Install from PyPI](#install-from-pypi)
- [From a source checkout](#from-a-source-checkout)
- [Using the library](#using-the-library)
- [Environment variables](#environment-variables)


## Install from PyPI

```
pip3 install diagnosticism
```

**Diagnosticism.Python** runs on **Python 2.7** and **Python 3.8+**. It has no runtime dependencies.


## From a source checkout

```
python3 -m pip install -e .
./run_all_unit_tests.sh
```

On **Python 2.7** the unit tests need **mock**, and are run with `python tests/run_unittest.py`.


## Using the library

```Python
import diagnosticism
import diagnosticism.severity as sev

diagnosticism.enable_logging(True)
diagnosticism.log(sev.INFO, "hello")
```

To send records to the standard `logging` module instead of standard error:

```Python
import logging
import diagnosticism as d
import diagnosticism.severity as sev

logging.basicConfig(level=logging.DEBUG)
d.enable_logging(True)
d.set_log_logger(logging.getLogger('app'))
d.log(sev.INFO, "hello")
```

See [examples/set_log_logger.py](./examples/set_log_logger.py).


## Environment variables

On import, the first recognised value wins in each list:

* enable logging: `DIAGNOSTICISM_ENABLE_LOGGING`, `SIS_ENABLE_LOGGING`, `ENABLE_LOGGING`;
* enable tracing: `DIAGNOSTICISM_ENABLE_TRACING`, `SIS_ENABLE_TRACING`, `ENABLE_TRACING`;
* logging threshold: `DIAGNOSTICISM_LOGGING_THRESHOLD`, `SIS_LOGGING_THRESHOLD`, `LOGGING_THRESHOLD`, `SIS_SEVERITY_CEILING`;
* flush threshold: `DIAGNOSTICISM_FLUSH_THRESHOLD`, `SIS_FLUSH_THRESHOLD`, `FLUSH_THRESHOLD`, `SIS_FLUSH_CEILING`;


<!-- ########################### end of file ########################### -->
