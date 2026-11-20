# Diagnosticism.Python - Installation and Use <!-- omit in toc -->


## Table of Contents <!-- omit in toc -->

- [Install from PyPI](#install-from-pypi)
- [From a source checkout](#from-a-source-checkout)
- [Using the library](#using-the-library)


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


<!-- ########################### end of file ########################### -->
