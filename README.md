# cookiecutter-pypippackage

A Cookiecutter template for a [PyPI](https://pypi.python.org/) compatible, `pip` installable Python package with unit tests.

[Cookiecutter](https://github.com/audreyr/cookiecutter) is a command-line utility that creates projects from cookiecutters (project templates).


# Installation of Cookiecutter

You need to have Python, `pip` and Cookiecutter to use _cookiecutter-pypippackage_.
This section assumes that you have Python and `pip`, and shows the installation of Cookiecutter.

To install Cookiecutter:

```sh
pip install cookiecutter
```

Don't you have `pip`?
See the
[installation guide of `pip`](https://pip.pypa.io/en/stable/installing/).


# Usage of cookiecutter-pypippackage

After installing Cookiecutter, you can use _cookiecutter-pypippackage_ with the following command:

```sh
cookiecutter https://github.com/caglartoklu/cookiecutter-pypippackage.git
```


# Testing

After creating the package, tests can be executed with the following command at the root folder of the package:

```sh
python setup.py test
```

The testing framework of choice is [nose](https://nose.readthedocs.io/en/latest/).


# FAQ

### What is the Python version for the resulting package ?

The resulting package is fully tested with Python 3.
Python 2 is not supported yet, but it is on the way.

### How can I edit the `README.rst` file of the resulting package ?

PyPI supports reStructuredText by default instead of Markdown.
That is why the resulting package has a `README.rst` file instead of `README.md`.
You can use any editor for reStructuredText such as Vim, Emacs, Sublime Text etc.
If you want a specific editor, you can check [ReText](https://github.com/retext-project/retext).
If you need an online editor without any installation and configuration, you can use [rsted](https://github.com/anru/rsted).

### I don't like this package, it is too simple/complex/good/bad/ugly for me. Are there any alternatives for Python packages?

There is [cookiecutter-pypackage](https://github.com/audreyr/cookiecutter#cookiecutter-specials)
which is maintained by Cookiecutter team.
And [some others](https://github.com/audreyr/cookiecutter#python) too.


# Checklist after Creating the Package

- [ ] Run the tests.
- [ ] Check the `setup.py` content.
- [ ] Check the `tox.ini` content and remove unsupported Python versions.
- [ ] Edit the resulting `README.rst` content.


# License

This Cookiecutter template itself is licensed with MIT.
See the [LICENSE.txt](LICENSE.txt).

The package you create with this Cookiecutter template has the MIT license by default,
but it can be freely changed after creating the package.
