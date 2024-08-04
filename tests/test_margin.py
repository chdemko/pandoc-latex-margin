from unittest import TestCase
from panflute import convert_text, debug

import pandoc_latex_margin


class MarginTestCase(TestCase):
    def verify_conversion(
        self,
        text,
        expected,
        transform,
        input_format="markdown",
        output_format="latex",
        standalone=False,
    ) -> None:
        """
        Verify the conversion.

        Parameters
        ----------
        text
            input text
        expected
            expected text
        transform
            filter function
        input_format
            input format
        output_format
            output format
        standalone
            is the output format standalone ?
        """
        doc = convert_text(text, input_format=input_format, standalone=True)
        doc.format = output_format
        doc = transform(doc)
        converted = convert_text(
            doc.content,
            input_format="panflute",
            output_format=output_format,
            extra_args=["--wrap=none"],
            standalone=standalone,
        )
        print(converted)
        self.assertEqual(converted.strip(), expected.strip())

    def test_margin(self):
        self.verify_conversion(
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
\begin{pandocchangemargin}{1cm}{2cm}

Content1

\end{pandocchangemargin}

\begin{pandocchangemargin}{2cm}{1cm}

Content2

\end{pandocchangemargin}

\begin{pandocchangemargin}{0pt}{2cm}

Content3

\end{pandocchangemargin}

\begin{pandocchangemargin}{2cm}{0pt}

Content4

\end{pandocchangemargin}
            """,
            pandoc_latex_margin.main,
        )
