# Diagnosticism.Python <!-- omit from toc -->

Diagnosticism library, for Python

[![PyPI version](https://badge.fury.io/py/diagnosticism.svg)](https://badge.fury.io/py/diagnosticism)


## Table of Contents <!-- omit from toc -->

- [Introduction](#introduction)
- [Installation \& usage](#installation--usage)
- [Components](#components)
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


## Examples

Examples are provided in the ```examples``` directory, along with a markdown description for each. A detailed list TOC of them is provided in [EXAMPLES.md](./EXAMPLES.md).


## Project Information


### Where to get help

[GitHub Page](https://github.com/synesissoftware/Diagnosticism.Python "GitHub Page")


### Contribution guidelines

Defect reports, feature requests, and pull requests are welcome on https://github.com/synesissoftware/Diagnosticism.Python.


### Dependencies


### Related projects

* [**Diagnosticism**](https://github.com/synesissoftware/Diagnosticism/)
* [**Diagnosticism.Go**](https://github.com/synesissoftware/Diagnosticism.Go/)
* [**Diagnosticism.NET**](https://github.com/synesissoftware/Diagnosticism.NET/)


### License

**Diagnosticism.Python** is released under the 3-clause BSD license. See [LICENSE](./LICENSE) for details.



<!-- ########################### end of file ########################### -->

