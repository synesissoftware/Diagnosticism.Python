# Diagnosticism.Python <!-- omit from toc -->

Diagnosticism, for Python

![Language](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![PyPI](https://img.shields.io/pypi/v/diagnosticism.svg)](https://pypi.org/project/diagnosticism/)
[![GitHub release](https://img.shields.io/github/v/release/synesissoftware/Diagnosticism.Python.svg)](https://github.com/synesissoftware/Diagnosticism.Python/releases/latest)
![Python](https://img.shields.io/badge/Python-2.7%20%7C%203.8+-lightgrey)
[![CI](https://github.com/synesissoftware/Diagnosticism.Python/actions/workflows/python-package.yml/badge.svg)](https://github.com/synesissoftware/Diagnosticism.Python/actions/workflows/python-package.yml)
[![PyPI project](https://img.shields.io/badge/documentation-PyPI-lightgrey)](https://pypi.org/project/diagnosticism/)


## Table of Contents <!-- omit from toc -->

- [Introduction](#introduction)
- [Installation \& usage](#installation--usage)
	- [Python version compatibility](#python-version-compatibility)
- [Components](#components)
	- [Classes](#classes)
		- [`DOOMGram`](#doomgram)
		- [`DOOMScope`](#doomscope)
	- [Constants](#constants)
		- [Diagnostic Logging API](#diagnostic-logging-api)
		- [Contingent Reporting API](#contingent-reporting-api)
	- [Context Managers](#context-managers)
	- [Decorators](#decorators)
		- [`asynctracefunc`](#asynctracefunc)
		- [`tracefunc`](#tracefunc)
	- [Functions](#functions)
		- [Contingent Reporting API](#contingent-reporting-api-1)
		- [Debugging API](#debugging-api)
		- [Diagnostic Logging API](#diagnostic-logging-api-1)
		- [Tracing API](#tracing-api)
		- [Time formatting API](#time-formatting-api)
- [Examples](#examples)
- [Project Information](#project-information)
	- [Where to get help](#where-to-get-help)
	- [Contribution guidelines](#contribution-guidelines)
	- [Dependencies](#dependencies)
		- [Efferent (fan-out)](#efferent-fan-out)
			- [Development Dependencies](#development-dependencies)
		- [Afferent (fan-in)](#afferent-fan-in)
	- [Related projects](#related-projects)
	- [License](#license)


## Introduction

**Diagnosticism** is a standalone library of simple components for aiding in diagnostics for Python projects. It contains versions of components seen in the other **Diagnosticism**s - see [below](#related-projects) - though there is not a 1-to-1 correspondence between any of them.


## Installation & usage

Install via **pip** or **pip3**, as in:

```
$ pip3 install diagnosticism
```

Use via **import**:

```Python

import diagnosticism
```

When using the simple logging facilities, we find it convenient to import as follows:

```Python

import diagnosticism as d
import diagnosticism.severity as sev
```

that may then be used as:

```Python

d.log(sev.INFO, "hello")
```


### Python version compatibility

**Diagnosticism.Python** is intended to run on **Python 2.7** and **Python
3.8+**. GitHub Actions exercises **Python 2.7** and **Python 3.8–3.13**.

| Requirement | Applies to |
| ----------- | ---------- |
| Python **2.7** or **3.8+** | Core contingent reporting, logging, tracing, and severity APIs |
| Python **3.9+** | `@tracefunc` and `@asynctracefunc` decorators |

The public API surface is listed in `diagnosticism.__all__`.


## Components

**Diagnosticism.Python** provides components in the following categories:

* Contingent Reporting
* Diagnostic Logging
* Time formatting
* Tracing

**NOTE**: for the moment, the Diagnostic Logging facilities emit to the standard error stream, via the Contingent Reporting API. In the near future this will be changed to work with more sophisticated logging libraries, including the standard logging facilities and the (as yet to be release) **Pantheios.Python**.


### Classes

The following classes are defined:

#### `DOOMGram`

`DOOMGram` - Decimal Order-Of-Magnitude frequency histoGRAM - is a class for recording order-of-magnitude of operation timings, and then rendering the results in a text-based histogram format, as in:

#### `DOOMScope`

`DOOMScope` is a context-manager for use with `DOOMGram` for measuring scoped chunks of logic.

The example program [**examples/doomgram.py**](./examples/doomgram.py) illustrates these two types in combination

```Python
# examples/doomgram.py

def main():

    dg = DOOMGram()

    for _ in range(1_000):

        r = random.uniform(1, 1_000)

        d = r / 1_000_000

        with DOOMScope(dg):

            time.sleep(d)

    print("dg:", dg)

. . .
```

and produces output such as:

```bash
dg: ___abcc_____
```

which indicates the following breakdown of operation - in this case a random `sleep()` - timings:

| Time period(s) | Number of events in that period |
| ----------- | ------------ |
| Nanoseconds | no records   |
| Microseconds | 1-9 in 1µs (`a`); 10-99 in 10µs (`b`); 100-899 in 100µs (`c`) |
| Milliseconds | 100-999 in 1ms (`c`) |
| Seconds | no records  |


### Constants

#### Diagnostic Logging API

The following constants are defined:

| Constant | API | Purpose |
| -------- | --- | ------- |
| STOCK_TRAILING_PROMPT | **Contingent Reporting** | The stock trailing prompt, which is defined as `"use --help for usage"`. |

#### Contingent Reporting API

The following constants are defined:

| Constant | API | Purpose |
| -------- | --- | ------- |
| VIOLATION       | **Diagnostic Logging** | Severity level suitable for use when logging that a design violation has occurred. |
| ALERT           | **Diagnostic Logging** | Severity level suitable for use when logging that a fatal program failure has occurred. |
| CRITICAL        | **Diagnostic Logging** | Severity level suitable for use when logging that a critical failure has occurred. |
| FAILURE         | **Diagnostic Logging** | Severity level suitable for use when logging that a failure has occurred. |
| WARNING         | **Diagnostic Logging** | Severity level suitable for use when issuing a warning. |
| NOTICE          | **Diagnostic Logging** | Severity level suitable for use when logging an important normative condition. |
| INFORMATIONAL   | **Diagnostic Logging** | Severity level suitable for use when logging a normative condition. |
| DEBUG0          | **Diagnostic Logging** | The highest debug severity level. |
| DEBUG1          | **Diagnostic Logging** | The second highest debug severity level. |
| DEBUG2          | **Diagnostic Logging** | The third highest debug severity level. |
| DEBUG3          | **Diagnostic Logging** | The fourth highest debug severity level. |
| DEBUG4          | **Diagnostic Logging** | The fifth highest debug severity level. |
| DEBUG5          | **Diagnostic Logging** | The sixth highest debug severity level. |
| TRACE           | **Diagnostic Logging** | Severity level suitable at which trace statements are issued. |
| BENCHMARK       | **Diagnostic Logging** | Severity level suitable at which benchmark statements are issued. |
| DEBUG           | **Diagnostics Logging** | Alias for `DEBUG5` |
| FAIL            | **Diagnostics Logging** | Alias for `FAILURE` |
| WARN            | **Diagnostics Logging** | Alias for `WARNING` |
| INFO            | **Diagnostics Logging** | Alias for `INFORMATIONAL` |

> **NOTE**: all the severity level constants are for use with the `log()` function (as well as for setting/getting with `set_log_filter()` and `is_severity_logged()`).


### Context Managers

The following context managers are defined:

* `DOOMScope` - see [above](#doomscope);


### Decorators

The following decorators are defined:


#### `asynctracefunc`

Decorate that provides the equivalent functionality as `@tracefunc` for `async` functions and methods.


#### `tracefunc`

Decorator to be applied to functions and methods to save the need to call `d.trace()`, for example rather than:

```Python
def start():
	d.trace()
	. . .

def submit_work(name, job, priority=-1):
	d.trace()
	. . .
```

you can, more cleanly, write:

```Python
@d.tracefunc
def start():
	. . .

@d.tracefunc
def submit_work(name, job, priority=-1):
	. . .
```



### Functions

#### Contingent Reporting API

The following functions are defined:

| Function | Purpose |
| -------- | ------- |
| `abort()` | Issues a contingent report (via `conrep()`) and then terminating the process. |
| `report()` | Issues a message string as a contingent report, by defaulting writing output to `sys.stderr`. |
| `set_default_trailing_prompt()` | Sets the default trailing prompt. |
| `warn()` | An analogue to **Ruby**'s `warn()`, this issues the given message(s) to (by default0 the standard error stream and, if logging is enabled, also `log()`s at `WARNING` severity level. |


#### Debugging API

| Function | Purpose |
| -------- | ------- |
| `file()` | Obtains the file in which the calling function is defined. |
| `fileline()` | Obtains the file+line in which the calling function is defined. |
| `filelinefunc()` | Obtains the file+line+function in which the calling function is defined. |
| `func()` | Obtains the function in which the calling function is defined. |
| `line()` | Obtains the line on which the calling function is defined. |


#### Diagnostic Logging API

| Function | Purpose |
| -------- | ------- |
| `enable_logging()` | Enables/disables logging, whether from a constant or from a named environment variable. |
| `is_logging_enabled()` | Indicates whether logging is enabled. |
| `is_severity_logged()` | Indicates whether a log statement at a given severity will be logged. |
| `log()` | Submits a diagnostic log message at a given severity (which will be emitted in the case that `is_logging_enabled(sev))` would return `True`). |
| `set_log_filter()` | Sets a logging filter - either a threshold severity, or a `dict`` mapping severity levels to enablement flags - that allows fine-grained control of which levels are emitted. |


#### Tracing API

| Function | Purpose |
| -------- | ------- |
| `dbg()` | Similar to **Rust**'s `dbg!()` macro, can be passed any number of normal and keyword arguments and traces their name, type, and value. |
| `dbgfl()` | Like `dbg()`, but include `fileline()` information in the `TRACE` statement produced. |
| `enable_tracing()` | Enables/disables tracing, whether from a constant or from a named environment variable. |
| `is_tracing_enabled()` | Indicates whether tracing is enabled. |
| `trace()` | Traces the name and signature of the calling function, including the values of all its arguments. |


#### Time formatting API

| Function | Purpose |
| -------- | ------- |
| `nanoseconds_to_string()` | Formats a nanosecond count as a compact human-readable duration string, adapting the unit (`ns`, `µs`, `ms`, `s`) and decimal precision to keep roughly three significant digits in the numeric portion. Zero is always `"0s"`. An optional `format_spec` may include `'+'` to cause positive values to include an explicit leading sign. |

For example:

```Python
from diagnosticism import nanoseconds_to_string

nanoseconds_to_string(123_456_789)       # '123.4ms'
nanoseconds_to_string(      6_789)       # '6.789µs'
nanoseconds_to_string(999_772_000, '+')  # '+999.7ms'
```


## Examples

Examples are provided in the ```examples``` directory, along with a markdown description for each. A detailed list TOC of them is provided in [EXAMPLES.md](./EXAMPLES.md).


## Project Information


### Where to get help

[GitHub Page](https://github.com/synesissoftware/Diagnosticism.Python "GitHub Page")


### Contribution guidelines

Defect reports, feature requests, and pull requests are welcome on https://github.com/synesissoftware/Diagnosticism.Python.


### Dependencies

**Diagnosticism.Python** has no (non-development) runtime dependencies.


#### Efferent (fan-out)

Libraries upon which **Diagnosticism.Python** depends:

None.


##### Development Dependencies

* [**mock**](https://pypi.org/project/mock/) — required for running the unit-test suite on **Python 2.7**;


#### Afferent (fan-in)

Projects that depend on **Diagnosticism.Python**:

* [**asynkio**](https://github.com/synesissoftware/asynkio/);
* [**libpath.Python**](https://github.com/synesissoftware/libpath.Python/);


### Related projects

* [**Diagnosticism**](https://github.com/synesissoftware/Diagnosticism/) (**C**);
* [**Diagnosticism.Go**](https://github.com/synesissoftware/Diagnosticism.Go/);
* [**Diagnosticism.NET**](https://github.com/synesissoftware/Diagnosticism.NET/);
* [**Diagnosticism.Rust**](https://github.com/synesissoftware/Diagnosticism.Rust/);


### License

**Diagnosticism.Python** is released under the 3-clause BSD license. See [LICENSE](./LICENSE) for details.


<!-- ########################### end of file ########################### -->

