# Python module template

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code style: flake8](https://img.shields.io/badge/code%20style-flake8-1c4a6c.svg)](https://flake8.pycqa.org/en/latest/)

<!-- ![ci](https://github.com/Tomansion/Python-module-template/actions/workflows/pull-request-checks.yml/badge.svg) -->
<!-- ![cd](https://github.com/tomansion/Python-module-template/actions/workflows/continuous-deployment.yml/badge.svg) -->

---

This project is a template for Python module. It includes a basic example of functions that allows users to do some simple arithmetic operations.

## Template features

- Documentation:

  - [**Docstring**](https://www.python.org/dev/peps/pep-0257/): A way to document the code using comments.
  - [**Sphinx**](https://www.sphinx-doc.org/): A tool that makes it easy to create intelligent and beautiful documentation.

- Code Quality:

  - [**Black**](https://pypi.org/project/black/): A code formatters that automatically format the Python code.
  - [**Flake8**](https://flake8.pycqa.org/en/latest/): A tool that checks the code for style and quality.
  - [**Cspell**](https://cspell.org/): A spell checker that checks the spelling in the code, edit the [`cspell.json`](cspell.json) file to add custom words or languages.

- Testing:

  - [**Pytest**](https://docs.pytest.org/): A testing framework for Python that makes it easy to write small tests.

- Continuous Integration and Continuous Deployment:

  - **GitHub Actions**: This project includes a GitHub Actions workflow that runs the tests, linters, pushes the Python module to the PyPI repository, and deploys the documentation to GitHub Pages.

## Python module documentation

The documentation is available at [https://tomansion.github.io/Git-course-CentraleSupelec/](https://tomansion.github.io/Git-course-CentraleSupelec/).

## Getting started

To use this Python module template, follow these steps:

```bash
# Clone the repository
git clone https://github.com/Tomansion/Python-module-template.git

# Install the python module
cd Python-module-template
pip install .
```

## Test

To run the tests using Pytest, follow these steps:

```bash
# Install the required dependencies:
pip install -r requirements.txt

# Run the tests
pytest

# Run the tests with coverage
pytest --cov=python_module_template
```

## TODO

- [x] Create basic functions
- [x] Add unit tests with pytest
- [x] Add tests CI/CD pipeline
- [x] Add Sphinx documentation
- [x] Add documentation CI/CD pipeline with GitHub Pages
- [ ] Pipelines badges
- [ ] Coverage check pipeline and display in the README badge
- [ ] Add to Pypi
- [ ] Pypi upload pipeline
