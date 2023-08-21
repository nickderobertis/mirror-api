[![](https://codecov.io/gh/nickderobertis/mirror-api/branch/main/graph/badge.svg)](https://codecov.io/gh/nickderobertis/mirror-api)
[![PyPI](https://img.shields.io/pypi/v/mirror-api)](https://pypi.org/project/mirror-api/)
![PyPI - License](https://img.shields.io/pypi/l/mirror-api)
[![Documentation](https://img.shields.io/badge/documentation-pass-green)](https://nickderobertis.github.io/mirror-api/)
![Tests Run on Ubuntu Python Versions](https://img.shields.io/badge/Tests%20Ubuntu%2FPython-3.8%20%7C%203.9%20%7C%203.10-blue)
![Tests Run on Macos Python Versions](https://img.shields.io/badge/Tests%20Macos%2FPython-3.8%20%7C%203.9%20%7C%203.10-blue)
![Tests Run on Windows Python Versions](https://img.shields.io/badge/Tests%20Windows%2FPython-3.8%20%7C%203.9%20%7C%203.10-blue)
[![Github Repo](https://img.shields.io/badge/repo-github-informational)](https://github.com/nickderobertis/mirror-api/)

# mirror-api

## Overview

An API that returns the structure of the request as the response.

If you send it a request with any method to any path besides `/docs`,
it will return a response matching the structure of the request.

This is useful as a sample server to test infrastructure and ensure
that requests are being sent and received as expected.

## Getting Started

Install `mirror-api`:

```
pip install mirror-api
```

Simply run the `mirror-api` command to start the server. To see all available
options, run `mirror-api --help`.

## Links

See the
[documentation here.](https://nickderobertis.github.io/mirror-api/)

## Development Status

This project is currently in early-stage development. There may be
breaking changes often. While the major version is 0, minor version
upgrades will often have breaking changes.

## Developing

See the [development guide](https://github.com/nickderobertis/mirror-api/blob/main/DEVELOPING.md) for development details.

## Author

Created by Nick DeRobertis. MIT License.
