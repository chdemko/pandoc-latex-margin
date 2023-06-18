# Installation

[![Python package](https://github.com/chdemko/pandoc-latex-margin/workflows/Python%20package/badge.svg?branch=develop)](https://github.com/chdemko/pandoc-latex-margin/actions/workflows/python-package.yml)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-latex-margin/develop.svg)](https://coveralls.io/github/chdemko/pandoc-latex-margin?branch=develop)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-latex-margin.svg)](https://scrutinizer-ci.com/g/chdemko/pandoc-latex-margin/)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-latex-margin.svg)](https://pypi.org/project/pandoc-latex-margin/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-latex-margin.svg)](https://pypi.org/project/pandoc-latex-margin/)
[![License](https://img.shields.io/pypi/l/pandoc-latex-margin.svg)](https://raw.githubusercontent.com/chdemko/pandoc-latex-margin/develop/LICENSE)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-latex-margin.svg)](https://pypi.org/project/pandoc-latex-margin/)
[![Poetry version](https://img.shields.io/badge/poetry-1.2%20|%201.3%20|%201.4%20|%201.5-blue.svg)](https://python-poetry.org/)
[![Pandoc version](https://img.shields.io/badge/pandoc-2.11%20|%202.12%20|%202.13%20|%202.14%20|%202.15%20|%202.16%20|%202.17%20|%202.18%20|%202.19%20|%203.0%20|%203.1-blue.svg)](https://pandoc.org/)
[![Development Status](https://img.shields.io/pypi/status/pandoc-latex-margin.svg)](https://pypi.org/project/pandoc-latex-margin/)
[![Docs](https://img.shields.io/readthedocs/pandoc-latex-margin.svg?logo=read-the-docs&logoColor=white)](http://pandoc-latex-margin.readthedocs.io/en/latest/)

*pandoc-latex-margin* is a [pandoc] filter for changing margin size to `CodeBlock` and `Div` that have speficied classes or `latex-left-margin` and `latex-right-margin` attributes.

[pandoc]: http://pandoc.org/

Instructions
------------

*pandoc-latex-margin* requires [python], a programming language that comes pre-installed on linux and Mac OS X, and which is easily installed [on Windows].

Install *pandoc-latex-margin* using the bash command

~~~shell
$ pip install pandoc-latex-margin
~~~

To upgrade to the most recent release, use

~~~shell
$ pip install --upgrade pandoc-latex-margin
~~~

To upgrade to the current code, use

~~~
$ pip install --upgrade --force git+https://github.com/chdemko/pandoc-latex-margin
~~~

`pip` is a script that downloads and installs modules from the Python Package Index, [PyPI].  It should come installed with your python distribution. If you are running linux, `pip` may be bundled separately. On a Debian-based system (including Ubuntu), you can install it as root using

    apt-get update
    apt-get install python3-pip

[python]: https://www.python.org
[on Windows]: https://www.python.org/downloads/windows
[PyPI]: https://pypi.org


Getting Help
------------

If you have any difficulties with *pandoc-latex-margin*, please feel welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-latex-margin/issues

