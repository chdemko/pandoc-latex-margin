Installation
============

[![Python package](https://img.shields.io/github/actions/workflow/status/chdemko/pandoc-latex-margin/python-package.yml?logo=github&branch=develop)](https://github.com/chdemko/pandoc-latex-margin/actions/workflows/python-package.yml)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://pypi.org/project/black/)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-latex-margin/develop.svg?logo=Codecov&logoColor=white)](https://coveralls.io/github/chdemko/pandoc-latex-margin?branch=develop)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-latex-margin.svg?logo=scrutinizer)](https://scrutinizer-ci.com/g/chdemko/pandoc-latex-margin/)
[![Code Climate](https://img.shields.io/codeclimate/maintainability/chdemko/pandoc-latex-margin?logo=codeclimate&barnch=develop)](https://codeclimate.com/github/chdemko/pandoc-latex-margin/)
[![CodeFactor](https://img.shields.io/codefactor/grade/github/chdemko/pandoc-latex-margin/develop.svg?logo=codefactor)](https://www.codefactor.io/repository/github/chdemko/pandoc-latex-margin)
[![Codacy](https://img.shields.io/codacy/grade/7df59d426cab4adca51d86403f0cc4b6.svg?logo=codacy)](https://app.codacy.com/gh/chdemko/pandoc-latex-margin/dashboard)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-latex-margin.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-margin/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-latex-margin.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-margin/)
[![License](https://img.shields.io/pypi/l/pandoc-latex-margin.svg?logo=pypi&logoColor=white)](https://raw.githubusercontent.com/chdemko/pandoc-latex-margin/develop/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/pandoc-latex-margin?logo=pypi&logoColor=white)](https://pepy.tech/project/pandoc-latex-margin)
[![Development Status](https://img.shields.io/pypi/status/pandoc-latex-margin.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-margin/)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-latex-margin.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-margin/)
[![Pandoc version](https://img.shields.io/badge/pandoc-2.11%20..%203.6-blue.svg?logo=markdown)](https://pandoc.org/)
[![Latest release](https://img.shields.io/github/release-date/chdemko/pandoc-latex-margin.svg?logo=github)](https://github.com/chdemko/pandoc-latex-margin/releases)
[![Last commit](https://img.shields.io/github/last-commit/chdemko/pandoc-latex-margin/develop?logo=github)](https://github.com/chdemko/pandoc-latex-margin/commit/develop/)
[![Repo Size](https://img.shields.io/github/repo-size/chdemko/pandoc-latex-margin.svg?logo=github)](http://pandoc-latex-margin.readthedocs.io/en/latest/)
[![Code Size](https://img.shields.io/github/languages/code-size/chdemko/pandoc-latex-margin.svg?logo=github)](http://pandoc-latex-margin.readthedocs.io/en/latest/)
[![Source Rank](https://img.shields.io/librariesio/sourcerank/pypi/pandoc-latex-margin.svg?logo=libraries.io&logoColor=white)](https://libraries.io/pypi/pandoc-latex-margin)
[![Docs](https://img.shields.io/readthedocs/pandoc-latex-margin.svg?logo=read-the-docs&logoColor=white)](http://pandoc-latex-margin.readthedocs.io/en/latest/)

*pandoc-latex-margin* is a [pandoc] filter for changing margin size to
`CodeBlock` and `Div` that have speficied classes or `latex-left-margin`
and `latex-right-margin` attributes.

[pandoc]: http://pandoc.org/

Instructions
------------

*pandoc-latex-margin* requires [python], a programming language that comes
pre-installed on linux and Mac OS X, and which is easily installed
[on Windows].

Install *pandoc-latex-margin* using the bash command

~~~shell-session
$ pipx install pandoc-latex-margin
~~~

To upgrade to the most recent release, use

~~~shell-session
$ pipx upgrade pandoc-latex-margin
~~~

`pipx` is a script to install and run python applications in isolated environments from the Python Package Index, [PyPI]. It can be installed using instructions given [here](https://pipx.pypa.io/stable/).

[python]: https://www.python.org
[on Windows]: https://www.python.org/downloads/windows
[PyPI]: https://pypi.org


Getting Help
------------

If you have any difficulties with *pandoc-latex-margin*, please feel welcome
to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-latex-margin/issues

Contribute
==========

Instructions
------------

Install `hatch`, then run

~~~shell-session
$ hatch run pip install pre-commit
$ hatch run pre-commit install
~~~

to install `pre-commit` before working on your changes.

Tests
-----

When your changes are ready, run

~~~shell-session
$ hatch test
$ hatch fmt --check
$ hatch run lint:check
$ hatch run docs:build
$ hatch build -t wheel
~~~

for running the tests, checking the style, building the documentation
and building the wheel.

