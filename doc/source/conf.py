"""
Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import sys
from pathlib import Path

sys.path.append(str(Path.cwd().parents[2].resolve() / "reverse_argparse"))

# -- Project information ------------------------------------------------------

project = "reverse_argparse"
copyright = (  # noqa: A001
    "2023, National Technology & Engineering Solutions of Sandia, LLC (NTESS)"
)
author = "Jason M. Gates"
version = "1.0.8"
release = version

# -- General configuration ----------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    "sphinx_rtd_theme",
    "sphinxcontrib.programoutput",
    "sphinxcontrib.spelling",
]
intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

templates_path = ["_templates"]


# -- Options for HTML output --------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# -- AutoDoc Configuration ----------------------------------------------------

autodoc_default_options = {
    "show-inheritance": True,
    "members": True,
    "undoc-members": True,
}
autoclass_content = "both"
autodoc_preserve_defaults = True
autodoc_inherit_docstrings = False
