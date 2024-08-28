.. Photoneo Sphinx Docs Generator documentation master file, created by
   sphinx-quickstart on Wed May 17 07:45:09 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Photoneo Docs!
=================================================

* Jenkins Job is called `Product/Sphinx Docs`_.
* GitHub PR is `photoneo/sphinx_doc#1`_.

Read about `reStructuredText`_ on official `Sphinx docs`_. Choose a theme from `sphinx-themes.org`_.

To build manually, install Python and run the following commands (if you are on Windows,
use Git Bash)::

    # initial setup
    python -m pip install poetry==1.8.3
    python -m venv .venv
    source ~/.venv/*/activate
    poetry install

    # rebuild after changing documentation files
    sphinx-build -b html source/ build/

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   docs/p3dm
   docs/p3dm/introduction
   docs/p3dm/getting_started


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _Product/Sphinx Docs: http://jenkins-test.photoneo.com/job/Product/job/Sphinx%20Docs/
.. _photoneo/sphinx_doc#1: https://github.com/photoneo/sphinx_doc/pull/1
.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html
.. _Sphinx docs: https://www.sphinx-doc.org/en/master/index.html
.. _sphinx-themes.org: https://sphinx-themes.org/#themes
