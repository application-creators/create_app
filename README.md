<p align="center">
  <img alt="Create App logo" src="https://raw.githubusercontent.com/application-creators/create_app/main/docs/static/logo-cropped.png">
</p>

<p align="center">
    <a href="https://github.com/application-creators/create_app/actions"><img alt="Test Workflow Status" src="https://github.com/application-creators/create_app/workflows/Test/badge.svg"></a>
    <a href="https://github.com/application-creators/create_app/actions"><img alt="Linting Workflow Status" src="https://github.com/application-creators/create_app/workflows/Lint/badge.svg"></a>
    <a href="https://github.com/application-creators/create_app/actions"><img alt="PyPI Publication Workflow Status" src="https://github.com/application-creators/create_app/workflows/Publish%20to%20PyPI/badge.svg"></a>
    <a href="https://coveralls.io/github/application-creators/create_app?branch=main"><img alt="Coverage Status" src="https://coveralls.io/repos/github/application-creators/create_app/badge.svg?branch=main"></a>
    <!-- <a href="https://github.com/application-creators/create_app/blob/main/LICENSE"><img alt="License: MIT" src="https://create_app.readthedocs.io/en/stable/_static/license.svg"></a> -->
    <!-- <a href="https://create_app.readthedocs.io/en/stable/?badge=stable"><img alt="Documentation Status" src="https://readthedocs.org/projects/create_app/badge/?version=stable"></a>  -->
    <a href="https://pypi.org/project/create_app/"><img alt="PyPI" src="https://img.shields.io/pypi/v/create_app"></a>
    <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

_create_app_ is a tool for creating applications from templates.

When developers start a new project, they perform some repetitive tasks to build the basic project structure before 
actually start coding features. This basic structure involves things like: Well, the project structure, unit testing, 
code coverage, containerization, code linting and formatting, GIT hooks, building code documentation, among many others. 

_create_app_ is a tool that allows to quickly get your basic project structure ready. It provides a set of templates
from which you can get your project started, plus it's super easy to use and encourages the adoption of the best 
technologies, tools, and practices. 

At the moment, there are only Python templates available. But _create_app_ can generate projects of **any language**.


## Installation

Just install it with PIP:
```shell
python -m pip install create_app
```

## Usage

Run this command to generate your project:
```shell
create_app [template_name]
```

Or:
```shell
python -m create_app [template_name]
```

If you don't provide the _template_name_ argument, it defaults to "python_simple".


## Index of Available Templates

There's an [index of templates](/templates.json), from which you can get your project started:

| **Template**                                                                                         | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [python_simple](https://github.com/application-creators/python_simple)                               | Python project with unit tests, GIT hooks ([pre-commit](https://pre-commit.com/), [black](https://github.com/psf/black), [isort](https://pycqa.github.io/isort/), and [flake8](https://flake8.pycqa.org/en/latest/)), and Docker                                                                                                                                                                                                                   |
| [python_compose](https://github.com/application-creators/python_compose)                             | Python project with unit tests, GIT hooks ([pre-commit](https://pre-commit.com/), [black](https://github.com/psf/black), [isort](https://pycqa.github.io/isort/), and [flake8](https://flake8.pycqa.org/en/latest/)), and Docker Compose                                                                                                                                                                                                           |
| [python_fastapi](https://github.com/application-creators/python_fastapi)                             | FastAPI project with unit tests, GIT hooks ([pre-commit](https://pre-commit.com/), [black](https://github.com/psf/black), [isort](https://pycqa.github.io/isort/), and [flake8](https://flake8.pycqa.org/en/latest/)), and Docker                                                                                                                                                                                                                  |
| [python_fastapi_with_database](https://github.com/application-creators/python_fastapi_with_database) | FastAPI project with unit tests, GIT hooks ([pre-commit](https://pre-commit.com/), [black](https://github.com/psf/black), [isort](https://pycqa.github.io/isort/), and [flake8](https://flake8.pycqa.org/en/latest/)), Docker Compose, a [PostgreSQL](https://www.postgresql.org/) database (which can be very easily changed for any other), [SQLAlchemy](https://www.sqlalchemy.org/), and [Alembic](https://alembic.sqlalchemy.org/) migrations |


## Contribute

[Application Creators](https://github.com/application-creators) is a new GitHub organization I've created to host, 
debate, and maintain this tool and the project templates. Its goal is to generate state-of-the-art templates useful 
to everyone. Feel free to express you opinion and contribute!
