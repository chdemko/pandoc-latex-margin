# pandoc-latex-margin
[![Build Status](https://img.shields.io/travis/chdemko/pandoc-latex-margin/master.svg)](https://travis-ci.org/chdemko/pandoc-latex-margin/branches)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-latex-margin/master.svg)](https://coveralls.io/github/chdemko/pandoc-latex-margin?branch=master)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-latex-margin.svg)](https://scrutinizer-ci.com/g/chdemko/pandoc-latex-margin/)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-latex-margin.svg)](https://pypi.org/project/pandoc-latex-margin/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-latex-margin.svg)](https://pypi.org/project/pandoc-latex-margin/)
[![License](https://img.shields.io/pypi/l/pandoc-latex-margin.svg)](https://raw.githubusercontent.com/chdemko/pandoc-latex-margin/master/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/pandoc-latex-margin.svg)](https://pypi.org/project/pandoc-latex-margin/)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-latex-margin.svg)](https://pypi.org/project/pandoc-latex-margin/)
[![Development Status](https://img.shields.io/pypi/status/pandoc-latex-margin.svg)](https://pypi.org/project/pandoc-latex-margin/)

*pandoc-latex-margin* is a [pandoc] filter for changing margin size to `CodeBlock` and `Div` that have speficied classes or `latex-left-margin` and `latex-right-margin` attributes.

[pandoc]: http://pandoc.org/

Documentation
-------------

See the [wiki pages](https://github.com/chdemko/pandoc-latex-margin/wiki).

Usage
-----

To apply the filter, use the following option with pandoc:

    --filter pandoc-latex-margin

Installation
------------

*pandoc-latex-margin* requires [python], a programming language that comes pre-installed on linux and Mac OS X, and which is easily installed [on Windows]. Either python 2.7 or 3.x will do.

Install *pandoc-latex-margin* as root using the bash command

    pip install pandoc-latex-margin

To upgrade to the most recent release, use

    pip install --upgrade pandoc-latex-margin

To upgrade to the current code, use

    pip install --upgrade --force git+https://github.com/chdemko/pandoc-latex-margin

`pip` is a script that downloads and installs modules from the Python Package Index, [PyPI].  It should come installed with your python distribution. If you are running linux, `pip` may be bundled separately. On a Debian-based system (including Ubuntu), you can install it as root using

    apt-get update
    apt-get install python-pip

[python]: https://www.python.org
[on Windows]: https://www.python.org/downloads/windows
[PyPI]: https://pypi.org


Getting Help
------------

If you have any difficulties with *pandoc-latex-margin*, please feel welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-latex-margin/issues

