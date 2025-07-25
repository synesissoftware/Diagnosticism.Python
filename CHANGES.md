# **Diagnosticism.Python** Changes

## 0.13.0 - 25th July 2025

* `abort()`, `log()`, `report()`, `trace()`, `warn()` now each take `file` optional parameter;
* `warn()` can take multiple strings (a la **Ruby**'s `warn()`);


## 0.12.1 - 25th July 2025

* `DOOMScope` now uses `time.perf_counter_ns()`;


## 0.12.0 - 20th July 2025

* added `DOOMGram` and `DOOMScope`;


## 0.11.1 - 19th July 2025

* ~ fix to `warn()` (when logging is enabled);


## 0.11.0 - 18th July 2025

* ~ `enable_logging()` now also takes 2-parameters (environment variable name(s), default value) as well as 1-parameter (is_enabled);
* ~ `enable_tracing()` now also takes 2-parameters (environment variable name(s), default value) as well as 1-parameter (is_enabled);


## 0.10.1 - 17th July 2025

* ~ fixed package error;


## 0.10.0 - 14th July 2025

* + added `file()`, `line()`, `func()`, `fileline()`, `filelinefunc()`;
* + added `dbg()`, `dbgfl()`;


## 0.9.1 - 6h July 2025

* ~ fixed erroneous behaviour of `trace()` when used in module context


## 0.9.0 - 20th August 2024

* + added `parse_severity()`


## 0.8.0 - 17th August 2024

* + added `is_severity_logged()`


## 0.7.3 - 16th August 2024

* ~ fixed filter logic


## 0.7.2 - 16th August 2024

* ~ ANSI sequences on Windows 11+ (from build 22000 onwards)


## 0.7.1 - 15th August 2024

* + added missing `set_log_filter` export to top-level module
* ~ ANSI sequences on Windows 10+


## 0.7.0 - 14th August 2024

* ~ numerous changes to module names, including `diagnosticism.log` => `diagnosticism.logging`, to avoid name conflicts with functions (such as `log()` and `trace()`);
* ~ scripts now all assume **python3** executable, rather than **python**;


## 0.6.1 - 28th August 2020

* ~ fixed recently introduced defect in ``enable_tracing()``


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


<!-- ########################### end of file ########################### -->

