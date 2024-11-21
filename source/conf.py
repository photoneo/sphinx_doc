# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Knowledge Base'
copyright = '2024, Photoneo s.r.o'
author = 'Photoneo s.r.o.'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


import sphinx_rtd_theme
import os
import pathlib
import sys
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())
sys.setrecursionlimit(1500)

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx_rtd_theme',
    'sphinx.ext.autosummary',
    'sphinx_tabs.tabs',
    'sphinx_panels',
    'sphinxcontrib.youtube',
    'sphinx_copybutton',]

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
}

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'searchbox.html',
    ]
}


templates_path = ['_templates']
exclude_patterns = []

extlinks = {
    'envvar': ('https://docs.python.org/3/library/os.html#os.environ', '')
}



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
