# release_auditor
[![PyPI version](https://badge.fury.io/py/release_auditor.svg)](https://badge.fury.io/py/release_auditor)
[![Build Status](https://github.com/nightwatchcybersecurity/release_auditor/workflows/Test%20package/badge.svg?branch=master)](https://github.com/nightwatchcybersecurity/release_auditor/actions)
[![codecov](https://codecov.io/gh/nightwatchcybersecurity/release_auditor/branch/master/graph/badge.svg)](https://codecov.io/gh/nightwatchcybersecurity/release_auditor)
![GitHub](https://img.shields.io/github/license/nightwatchcybersecurity/release_auditor.svg)

A tool for checking if GitHub release assets were modified after publication.

For more information, [please read our blog post here](https://wwws.nightwatchcybersecurity.com/2021/04/25/supply-chain-attacks-via-github-com-releases/).

## Requirements
Python 3 is required and you can find all required modules in the **requirements.txt** file.
Only tested on Python 3.7 but should work on other 3.x releases.

## Installation
You can install this via PIP as follows:
```
pip install release_auditor
release_auditor --version
```
To download and run manually, do the following:
```
git clone https://github.com/nightwatchcybersecurity/release_auditor.git
cd release_auditor
pip install -r requirements.txt
python -m release_auditor.cli
```

## How to use
This utility is intended to check if a GitHub release was modified afer publication. This utility
will not check source code archives included with a release because they are immutable. It does
two checks on release assets:
1. Whether the asset was created/modified by someone else other than the release author.
2. Whether the asset was created/modified after initial publication.

By default, the 5 most recent releases are checked and the time interval checked is 24 hours. You can
override both via the "--max" and "--hours" options.

A non-zero error code will be returned after execution if any issues are found.

## Additional options 
By default, this utility accesses GitHub anonymously, which can result in API rate limiting. Consider
running this less often or pass in a GitHub username/password/access token via the "--login_or_token"
and "--password" parameters.

You can use this with self-hosted GitHub instances by passing the instance URL via the "--base-url"
parameter. However, this has not been tested.

The "--verbose" option shows additional information during checking.

### Example use
Run as following:
```
release_auditor github nightwatchcybersecurity/truegaze
```

The following results will be returned:
```
Retrieving repository and release information
Checking the first 5 releases

Checking release: Version 0.1.7 released

Checking release: Version 0.1.6 released

Checking release: Version 0.1.5 released

Checking release: Version 0.1.4 released

Checking release: Version 0.1.3 released
```
# Development Information

## Reporting bugs and feature requests
Please use the GitHub issue tracker to report issues or suggest features:
https://github.com/nightwatchcybersecurity/release_auditor

You can also send emai to ***research /at/ nightwatchcybersecurity [dot] com***

## Wishlist
- Add unit tests
- TBD
