# **Diagnosticism.Python** Changes

## 0.6.0 - 28th August 2020

* + added ``set_log_filter()``, which takes a severity-level as a threshold or a dictionary that controls emission of individual severity-levels

## 0.5.1 - 28th August 2020

* + added more documentation and parameter assertions

## 0.5.0 - 13th August 2020

* ~ ``log()`` now can take a message lamba as well as a message string

## 0.4.1 - 13th August 2020

* + added ``warn()`` (as an analogue of Ruby's ``Kernel#warn()``)
* + added ``conrep.set_default_usage_prompt()`` to allow a default usage prompt for ``abort()``
* ~ general improvements to documentation

## 0.4.0 - 11th July 2020

* ~ changed project name from **diagnosticism.Python** to **Diagnosticism.Python**
* + added **tests/test_conrep.py**

## 0.3.1 - 8th July 2019

* ~ ``abort()`` now applies ``str()`` on ``message`` param, to allow argument types such as exceptions

## 0.3.0 - 7th July 2019

* + added module ``diagnosticism.log``, with members ``enable_logging()``, ``is_logging_enabled()``, and ``log()``
* + added module ``diagnosticism.severity``, with members ``VIOLATION``, ``ALERT``, ... ``DEBUG5``, ``TRACE``

## 0.2.1 - 7th July 2019

* ~ fixed missing name ``report`` exported at top-level

## 0.2.0 - 7th July 2019

* + added module ``diagnosticism.program_name``, with members ``get_program_name()`` and ``set_program_name()``
* + added module ``diagnosticism.conrep``, with members ``abort()`` and ``report()``

## 0.1.2 - 12th June 2019

* ~ enhancing ``trace()`` to handle methods elegantly

## 0.1.1 - 11th June 2019

* + ``trace()``

## 0.0.1 - 12th February 2019

* + project boilerplate



## previous versions

T.B.C.



