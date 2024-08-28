# Photoneo Sphinx Docs Generator

This script uses sphinx python package to generate documentation from files stored
in source folder. Follow these steps:

- Add your doc files inside `/source` folder.
- Update docs tree structure in `/source/index.rst` file (replace `file1` and `file2` symbolic examples).
- Feel free to customize `/source/conf.py` config file.
- Run jenkins job.

# Syntax

Read about [reStructuredText] on official [Sphinx docs]. Choose a theme from [sphinx-themes.org].

# Manual build

If you want to generate documentation files from source locally:

- Do all the previous steps.
- Activate venv and install all dependencies based on `pyproject.toml`.
- Run script `sphinx-build -b html source/ build/`.
- Output docs will be stored in `/build` folder.

    python -m pip install poetry==1.8.3
    python -m venv .venv
    source ~/.venv/*/activate
    poetry install
    sphinx-build -b html source/ build/



[dot]: https://www.sphinx-doc.org/en/master/
[reStructuredText]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html
[Sphinx docs]: https://www.sphinx-doc.org/en/master/index.html
[sphinx-themes.org]: https://sphinx-themes.org/#themes
