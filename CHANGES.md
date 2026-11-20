# Diagnosticism.Python - Changes <!-- omit in toc -->


## 0.19.0-alpha1 - 22nd November 2026



## 0.18.3 - 21st November 2026

* fixes:
  * logging and tracing hold one lock across the enable flag, the log filter, and the line write;


## 0.18.2 - 20th November 2026

* fixes:
  * `enable_tracing()` now returns the previous enable value;
  * `set_program_name()` now returns the previous program name;
  * module-level `trace()` now reports the call line;
  * `func()` and `line()` now forward keyword arguments to the caller-location lookup;
  * `log()` now stringifies a non-string message;
  * `DEBUG` is now part of the public API, as an alias of `DEBUG5`;
  * `dbg()` and `dbgfl()` no longer trace the consumed `file` argument;
  * `set_log_filter()` now accepts a callable;
  * `warn()` now honours the log filter and accepts a callable message;
  * `@tracefunc` and `@asynctracefunc` are available on Python 2.7 and 3.8+;
  * `@tracefunc` keeps the wrapped name and docstring, accepts `file`, awaits coroutines, and does not treat `staticmethod` or `classmethod` as instance methods;
  * the `perf_counter_ns` fallback uses `time.monotonic()` when that function exists;
* performance:
  * added **tests/performance/bench_logging.py** for a manual timing run;
* lint:
  * **Ruff** also selects Bugbear; `E501` stays ignored, and `B904` stays ignored because `raise ... from` is not valid on Python 2.7;
  * inline type annotations and **py.typed** stay out while the package is parsed by Python 2.7;
* tests:
  * removed the empty **tests/stub.py**;
  * covered `abort()` process exit, Windows basename, a cleared log filter, two logging threads, and `@asynctracefunc`;
* continuous integration:
  * tests run on macOS, Ubuntu, and Windows;
  * Python 3.8 and 3.9 run on Ubuntu 22.04;
* documentation and boilerplate:
  * canonicalising **CHANGES.md**;
  * canonicalising **NEWS.md**;
  * corrected historical notes: `parse_verbosity()` in 0.9.0, and Python 3.14 compatibility in 0.17.0;
  * **README.md** constant catalogs now sit under the matching API headings;
  * added **INSTALL.md** and **FAQ.md**;
  * older changelog bullets now end with `;`;
* packaging:
  * `__version__` in **diagnosticism/__init__.py** is the only version string;
  * removed `universal = 1` from **setup.cfg**;


## 0.18.1 - 14th September 2026

* packaging, documentation, and CI modernisation (PEP 621 hybrid, canonical CI, **ruff**, helper scripts);


## 0.18.0 - 6th August 2026

* added `function()` alias for `func()`;

## 0.17.0 - 10th July 2026

* added `DOOMGram::to_mmm()` and `DOOMGram::to_nmmm()` — compact min/mean/max duration summaries using `nanoseconds_to_string()`;
* updated compatibility to Python 3.14;


## 0.16.0 - 27th June 2026

* added `nanoseconds_to_string()`;


## 0.15.3 - 27th June 2026

* added top-level `__all__` documenting the public API;
* replaced top-level star-imports with explicit imports;
* restoring broken Python 2.7 compatibility;
* removed `tests` and `examples` from installable package;
* fixed `_str2bool()` defect;
* added `python_requires` for Python 2.7 and Python 3.8+;
* general tidying;


## 0.15.2 - 27th August 2025

* project boilerplate;
* documentation;


## 0.15.1 - 24th August 2025

* Python version compatibility claims;
* Python 3.8 compatibility;
* GitHub Actions;
* badges;
* boilerplate;


## 0.15.0 - 13th August 2025

* added `asynctracefunc` decorator;


## 0.14.1 - 31st July 2025

* fixed `tracefunc`;


## 0.14.0 - 28th July 2025

* added `tracefunc` decorator;


## 0.13.0 - 25th July 2025

* `abort()`, `log()`, `report()`, `trace()`, `warn()` now each take `file` optional parameter;
* `warn()` can take multiple strings (a la **Ruby**'s `warn()`);


## 0.12.1 - 25th July 2025

* `DOOMScope` now uses `time.perf_counter_ns()`;


## 0.12.0 - 20th July 2025

* added `DOOMGram` and `DOOMScope`;


## 0.11.1 - 19th July 2025

* fix to `warn()` (when logging is enabled);


## 0.11.0 - 18th July 2025

* `enable_logging()` now also takes 2-parameters (environment variable name(s), default value) as well as 1-parameter (is_enabled);
* `enable_tracing()` now also takes 2-parameters (environment variable name(s), default value) as well as 1-parameter (is_enabled);


## 0.10.1 - 17th July 2025

* fixed package error;


## 0.10.0 - 14th July 2025

* added `file()`, `line()`, `func()`, `fileline()`, `filelinefunc()`;
* added `dbg()`, `dbgfl()`;


## 0.9.1 - 6th July 2025

* fixed erroneous behaviour of `trace()` when used in module context;


## 0.9.0 - 20th August 2024

* added `parse_verbosity()`;


## 0.8.0 - 17th August 2024

* added `is_severity_logged()`;


## 0.7.3 - 16th August 2024

* fixed filter logic;


## 0.7.2 - 16th August 2024

* ANSI sequences on Windows 11+ (from build 22000 onwards);


## 0.7.1 - 15th August 2024

* added missing `set_log_filter` export to top-level module;
* ANSI sequences on Windows 10+;


## 0.7.0 - 14th August 2024

* numerous changes to module names, including `diagnosticism.log` => `diagnosticism.logging`, to avoid name conflicts with functions (such as `log()` and `trace()`);
* scripts now all assume **python3** executable, rather than **python**;


## 0.6.1 - 28th August 2020

* fixed recently introduced defect in ``enable_tracing()``;


## 0.6.0 - 28th August 2020

* added ``set_log_filter()``, which takes a severity-level as a threshold or a dictionary that controls emission of individual severity-levels;


## 0.5.1 - 28th August 2020

* added more documentation and parameter assertions;


## 0.5.0 - 13th August 2020

* ``log()`` now can take a message lamba as well as a message string;


## 0.4.1 - 13th August 2020

* added ``warn()`` (as an analogue of Ruby's ``Kernel#warn()``);
* added ``conrep.set_default_usage_prompt()`` to allow a default usage prompt for ``abort()``;
* general improvements to documentation;


## 0.4.0 - 11th July 2020

* changed project name from **diagnosticism.Python** to **Diagnosticism.Python**;
* added **tests/test_conrep.py**;


## 0.3.1 - 8th July 2019

* ``abort()`` now applies ``str()`` on ``message`` param, to allow argument types such as exceptions;


## 0.3.0 - 7th July 2019

* added module ``diagnosticism.log``, with members ``enable_logging()``, ``is_logging_enabled()``, and ``log()``;
* added module ``diagnosticism.severity``, with members ``VIOLATION``, ``ALERT``, ... ``DEBUG5``, ``TRACE``;


## 0.2.1 - 7th July 2019

* fixed missing name ``report`` exported at top-level;


## 0.2.0 - 7th July 2019

* added module ``diagnosticism.program_name``, with members ``get_program_name()`` and ``set_program_name()``;
* added module ``diagnosticism.conrep``, with members ``abort()`` and ``report()``;


## 0.1.2 - 12th June 2019

* enhancing ``trace()`` to handle methods elegantly;


## 0.1.1 - 11th June 2019

* ``trace()``;


## 0.0.1 - 12th February 2019

* project boilerplate;


<!-- ########################### end of file ########################### -->

