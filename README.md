# Diagnosticism.Python <!-- omit from toc -->

<!--
[![CircleCI](https://circleci.com/gh/google/diagnosticism.svg?style=svg)](https://circleci.com/gh/google/diagnosticism)
-->
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![PyPI version](https://badge.fury.io/py/diagnosticism.svg)](https://badge.fury.io/py/diagnosticism)
![versions](https://img.shields.io/pypi/pyversions/diagnosticism.svg)
[![Python package](https://github.com/synesissoftware/Diagnosticism.Python/actions/workflows/python-package.yml/badge.svg)](https://github.com/synesissoftware/Diagnosticism.Python/actions/workflows/python-package.yml)
[![Last Commit](https://img.shields.io/github/last-commit/synesissoftware/Diagnosticism.Python)](https://github.com/synesissoftware/Diagnosticism.Python/commits/master)

Diagnosticism library, for Python


## Table of Contents <!-- omit from toc -->

- [Introduction](#introduction)
- [Installation \& usage](#installation--usage)
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
- [Examples](#examples)
- [Project Information](#project-information)
	- [Where to get help](#where-to-get-help)
	- [Contribution guidelines](#contribution-guidelines)
	- [Dependencies](#dependencies)
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



## Components

**Diagnosticism.Python** provides components in the following categories:

* Contingent Reporting
* Diagnostic Logging
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

    for _ in range(1000):

        r = random.uniform(1, 1000)

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

T.B.C.


#### `tracefunc`

T.B.C.





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
| `dbg()` | Similar to **Rust**'s `dbg!()` macro, any number of normal and keyword arguments and traces their type, value, and name. |
| `dbgfl()` | Like `dbg()`, but include `fileline()` information in the `TRACE` statement produced. |
| `enable_tracing()` | Enables/disables tracing, whether from a constant or from a named environment variable. |
| `is_tracing_enabled()` | Indicates whether tracing is enabled. |
| `trace()` | Traces the name and signature of the calling function, including the values of all its arguments. |


## Examples

Examples are provided in the ```examples``` directory, along with a markdown description for each. A detailed list TOC of them is provided in [EXAMPLES.md](./EXAMPLES.md).


## Project Information


### Where to get help

[GitHub Page](https://github.com/synesissoftware/Diagnosticism.Python "GitHub Page")


### Contribution guidelines

Defect reports, feature requests, and pull requests are welcome on https://github.com/synesissoftware/Diagnosticism.Python.


### Dependencies


### Related projects

* [**Diagnosticism**](https://github.com/synesissoftware/Diagnosticism/) (**C**);
* [**Diagnosticism.Go**](https://github.com/synesissoftware/Diagnosticism.Go/);
* [**Diagnosticism.NET**](https://github.com/synesissoftware/Diagnosticism.NET/);
* [**Diagnosticism.Rust**](https://github.com/synesissoftware/Diagnosticism.Rust/);


### License

**Diagnosticism.Python** is released under the 3-clause BSD license. See [LICENSE](./LICENSE) for details.


<!-- ########################### end of file ########################### -->

