# audearch

audearch is a simple audio fingerprinting system

[![GitHub version](https://badge.fury.io/gh/peijun%2Fauderch.svg)](https://badge.fury.io/gh/peijun%2Fauderch)
![Python application](https://github.com/audearch/audearch/workflows/Python%20application/badge.svg?branch=master)
[![codecov](https://codecov.io/gh/audearch/audearch/branch/master/graph/badge.svg)](https://codecov.io/gh/audearch/audearch)
[![Maintainability](https://api.codeclimate.com/v1/badges/3a68a57d0d25eedcb465/maintainability)](https://codeclimate.com/github/audearch/audearch/maintainability)

## Discription

It's a system that recognizes and searches for music, using a technology called audio fingerprinting. Based on.

## Requirements

- python 3.6+
- pip 20.1.1+
- MongoDB 1.21.2+

## Installation

Install the dependencies from setup.py

```
$ python setup.py install
```

You need to install MongoDB beforehand

## Usage

Register and search are designed to be used with the CUI.

```
$ python audearch/register.py
$ python audearch/search.py
```

You can also use the GUI using fastapi. The current version does not support search. fastapi can be used with the following commands You can.

```
$ python web/run.py
```

## Author

peijun
