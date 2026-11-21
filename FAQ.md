# Diagnosticism.Python - FAQ <!-- omit in toc -->

Further questions are welcome on the
[Issues](https://github.com/synesissoftware/Diagnosticism.Python/issues)
forum.


## Table of Contents <!-- omit in toc -->

- [Q1: "How do I install this library?"](#q1-how-do-i-install-this-library)
- [Q2: "Which Python versions are supported?"](#q2-which-python-versions-are-supported)
- [Q3: "What else do I need to install?"](#q3-what-else-do-i-need-to-install)
- [Q4: "How do I send records to the standard logging module?"](#q4-how-do-i-send-records-to-the-standard-logging-module)


## Q1: "How do I install this library?"

Install via **pip**:

```
pip3 install diagnosticism
```

See [INSTALL.md](./INSTALL.md) for a source checkout and a short usage example.


## Q2: "Which Python versions are supported?"

**Python 2.7** and **Python 3.8+**. The library is not supported on Python 3.0 through 3.7.


## Q3: "What else do I need to install?"

Nothing for normal use. The unit tests on **Python 2.7** need **mock**.


## Q4: "How do I send records to the standard logging module?"

Call `set_log_logger()` with a standard `logging.Logger`. Records without an
explicit `file` then go to that logger. Pass `None` to restore the standard
error stream. See [examples/set_log_logger.py](./examples/set_log_logger.py).


<!-- ########################### end of file ########################### -->
