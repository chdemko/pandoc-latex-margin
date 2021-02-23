# This Python file uses the following encoding: utf-8

from unittest import TestCase
from panflute import *

import pandoc_latex_margin


def conversion(markdown, format="markdown"):
    doc = convert_text(markdown, standalone=True)
    doc.format = format
    pandoc_latex_margin.main(doc)
    return doc


def verify_conversion(markdown, expected, format="markdown"):
    doc = conversion(markdown, format)
    text = convert_text(
        doc,
        input_format="panflute",
        output_format="markdown",
        extra_args=["--wrap=none"],
        standalone=True,
    )
    debug("**computed**")
    debug(text.strip())
    debug("**expected**")
    debug(expected.strip())
    assert text.strip() == expected.strip()


def test_margin():
    verify_conversion(
        """
---
pandoc-latex-margin:
  - classes: [left]
    left: 1cm
  - classes: [right]
    right: 1cm
---

::: {.left latex-right-margin="2cm"} :::
Content1
:::::::::::::::

::: {.right latex-left-margin="2cm"} :::
Content2
:::::::::::::::

::: {latex-right-margin="2cm"} :::
Content3
:::::::::::::::

::: {latex-left-margin="2cm"} :::
Content4
:::::::::::::::

        """,
        r"""
---
header-includes:
- |
  `\def\pandocchangemargin#1#2{\list{}{\rightmargin#2\leftmargin#1}\item[]}
  \let\endpandocchangemargin=\endlist
  `{=tex}
pandoc-latex-margin:
- classes:
  - left
  left: 1cm
- classes:
  - right
  right: 1cm
---

`\def\pandocchangemargin#1#2{\list{}{\rightmargin#2\leftmargin#1}\item[]}
\let\endpandocchangemargin=\endlist
`{=tex}

```{=tex}
\begin{pandocchangemargin}{1cm}{2cm}
```
::: {.left latex-right-margin="2cm"}
Content1
:::

```{=tex}
\end{pandocchangemargin}
```
```{=tex}
\begin{pandocchangemargin}{2cm}{1cm}
```
::: {.right latex-left-margin="2cm"}
Content2
:::

```{=tex}
\end{pandocchangemargin}
```
```{=tex}
\begin{pandocchangemargin}{0pt}{2cm}
```
::: {latex-right-margin="2cm"}
Content3
:::

```{=tex}
\end{pandocchangemargin}
```
```{=tex}
\begin{pandocchangemargin}{2cm}{0pt}
```
::: {latex-left-margin="2cm"}
Content4
:::

```{=tex}
\end{pandocchangemargin}
```
        """,
        "latex",
    )
