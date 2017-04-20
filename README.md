# Bugcrowd
[![Build Status](https://travis-ci.org/leifdreizler/bugcrowd.svg?branch=master)](https://travis-ci.org/leifdreizler/bugcrowd)[![PyPI](https://img.shields.io/pypi/v/bugcrowd.svg)]()

Python wrapper for the [Bugcrowd API](https://docs.bugcrowd.com/docs/authentication) by [Leif Dreizler](https://twitter.com/leifdreizler) and [Zach Sperske](https://twitter.com/zsperske). Leif does work at Bugcrowd, but this isn't an official Bugcrowd integration.

Currently contains all functionality except creating a submission. The recent changes to the submission form are going to get added to the API soon and we didn't want to spend time writing code that will soon be deprecated.

This was our first Python module, so beware! 👻

## Installation

`$ pip install bugcrowd`

## Examples

We have included a few examples in the `examples` folder, and plan to add more in the future. In the meantime you should visit the tests folder and review the test cases for usage.

## What's Missing

We intentionally left out functionality related to creating submissions. The Bugcrowd submission form has recently undergone significant changes and the API is slightly behind those changes. We'll update this later :)
 