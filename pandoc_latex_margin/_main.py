#!/usr/bin/env python

"""
Pandoc filter for changing margins in LaTeX.
"""
from __future__ import annotations

import re
from typing import Any

from panflute import (
    Doc,
    Element,
    MetaInlines,
    MetaList,
    RawBlock,
    RawInline,
    debug,
    run_filter,
)


# pylint:disable=line-too-long
def get_correct_margin(length: str) -> str:
    """
    Get the margin.

    Arguments
    ---------
    length
        A margin in LaTeX notation.

    Returns
    -------
    str
        A correct margin.
    """
    if (
        re.match(
            "^(-?([1-9][0-9]*)|0)(pt|mm|cm|in|ex|em|bp|pc|dd|cc|nd|nc|sp)$", length
        )
        is not None
    ):  # noqa: E501
        return length
    debug(
        "[WARNING] pandoc-latex-margin: "
        + length
        + " is not a correct LaTeX margin; using 0pt"
    )  # noqa: E501
    return "0pt"


# pylint: disable=inconsistent-return-statements
def margin(elem: Element, doc: Doc) -> list[Element] | None:
    """
    Add margin to element if needed.

    Arguments
    ---------
    elem
        A pandoc element
    doc
        The pandoc document

    Returns
    -------
    list[Element] | None
        A list of pandoc elements or None.
    """
    # Is it in the right format and is it a Div or CodeBlock?
    if doc.format in ("latex", "beamer") and elem.tag in ("Div", "CodeBlock"):
        left = None
        right = None

        # Get the classes
        classes = set(elem.classes)

        # Loop on all fontsize definition
        for definition in doc.defined:
            # Are the classes correct?
            if classes >= definition["classes"]:
                left = definition["left"]
                right = definition["right"]
                break

        # Is there a latex-margin-left attribute?
        if "latex-left-margin" in elem.attributes:
            left = get_correct_margin(elem.attributes["latex-left-margin"])

        # Is there a latex-margin-right attribute?
        if "latex-right-margin" in elem.attributes:
            right = get_correct_margin(elem.attributes["latex-right-margin"])

        if left is not None or right is not None:
            if left is None:
                left = "0pt"
            if right is None:
                right = "0pt"
            return [
                RawBlock(
                    "\\begin{pandocchangemargin}{" + left + "}{" + right + "}", "tex"
                ),  # noqa: E501
                elem,
                RawBlock("\\end{pandocchangemargin}", "tex"),
            ]
    return None


def prepare(doc: Doc) -> None:
    """
    Prepare the document.

    Arguments
    ---------
    doc
        The pandoc document
    """
    # Prepare the definitions
    doc.defined = []

    # Get the meta data
    meta = doc.get_metadata("pandoc-latex-margin")

    if isinstance(meta, list):
        # Loop on all definitions
        for definition in meta:
            # Verify the definition
            if (
                isinstance(definition, dict)
                and "classes" in definition
                and isinstance(definition["classes"], list)
            ):  # noqa: E501
                add_definition(doc.defined, definition)


def add_definition(defined: list[dict[str, Any]], definition: dict[str, Any]):
    """
    Add a definition.

    Arguments
    ---------
    defined
        A list of definition
    definition
        A new definition
    """
    # Get the classes
    classes = definition["classes"]

    # Get the left margin
    if "left" in definition:
        left = get_correct_margin(definition["left"])
    else:
        left = "0pt"

    # Get the left margin
    if "right" in definition:
        right = get_correct_margin(definition["right"])
    else:
        right = "0pt"

    # Add a definition
    defined.append({"classes": set(classes), "left": left, "right": right})


def finalize(doc: Doc) -> None:
    """
    Finalize the document.

    Arguments
    ---------
    doc
        The pandoc document
    """
    # Add header-includes if necessary
    if "header-includes" not in doc.metadata:
        doc.metadata["header-includes"] = MetaList()
    # Convert header-includes to MetaList if necessary
    elif not isinstance(doc.metadata["header-includes"], MetaList):
        doc.metadata["header-includes"] = MetaList(
            doc.metadata["header-includes"]
        )  # noqa: E501

    # Add useful LaTex definition
    doc.metadata["header-includes"].append(
        MetaInlines(
            RawInline(
                "\n".join(
                    [
                        "\\def\\pandocchangemargin#1#2{\\list{}{\\rightmargin#2\\leftmargin#1}\\item[]}",  # noqa: E501
                        "\\let\\endpandocchangemargin=\\endlist",
                        "",
                    ]
                ),
                "tex",
            )
        )
    )


def main(doc: Doc | None = None) -> Doc:
    """
    Process the transformation.

    Arguments
    ---------
    doc
        The pandoc document.

    Returns
    -------
    Doc
        The modified document.
    """
    return run_filter(margin, prepare=prepare, doc=doc, finalize=finalize)


if __name__ == "__main__":
    main()
