# Usage

To apply the filter, use the following option with pandoc:

~~~{prompt} bash
pandoc --filter pandoc-latex-margin
~~~

Explanation
-----------

In the metadata block, specific set of classes can be defined to specify the
margins for `div` and `codeblock` elements.

The metadata block add information using the `pandoc-latex-margin` entry by
a list of definitions:

~~~yaml
pandoc-latex-margin:
  - classes: [myclass]
    left: 1cm
    right: 2cm
~~~

The metadata block above is used to set the margins:

* to `1cm` for left margin on `div` and `codeblock` elements that have the
 `myclass` class;
* to `2cm` for right margin on `div` and `codeblock` elements that have the
  `myclass` class;

The margins specified must be expressed in LaTeX syntax.

It's also possible to set a specific LaTeX margin using the `latex-left-margin`
and `latex-right-margin` attributes.

