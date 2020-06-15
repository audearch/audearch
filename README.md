# auderch

auderch is a simple audio fingerprinting system

[![Build Status](https://travis-ci.com/peijun/auderch.svg?branch=master)](https://travis-ci.com/peijun/auderch)
[![codecov](https://codecov.io/gh/peijun/auderch/branch/master/graph/badge.svg?token=2B5UB7X01C)](https://codecov.io/gh/peijun/auderch)
[![Maintainability](https://api.codeclimate.com/v1/badges/5fa2258580cd1429f8f6/maintainability)](https://codeclimate.com/github/peijun/auderch/maintainability)

## Discription

It's a system that recognizes and searches for music, using a technology called audio fingerprinting. Based on.

## Requirements

- python 3.6+
- pip 20.1.1+

## Installation

Install the dependencies from setup.py

```
$ python setup.py install
```

You need to install MongoDB beforehand

## Usage

Register and search are designed to be used with the CUI.

```
$ python auderch/register.py
$ python auderch/search.py
```

You can also use the GUI using fastapi. The current version does not support search. fastapi can be used with the following commands You can.

```
$ python web/run.py
```

## Author

peijun
