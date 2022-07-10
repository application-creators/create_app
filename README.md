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

Learn how to use the _create_app_ command:
```shell
python -m create_app --help
```

You can use the _--help_ option for all subcommands too.


### List templates

Use the _list_ subcommand to know which templates you can use:

```shell
python -m create_app list
```


### Create your project from a template

Use the _create_ subcommand and specify the _TEMPLATE_NAME_ you wish to use:
```shell
create_app create TEMPLATE_NAME
```


### Use a custom templates index

You or your organization may need to keep a separate index with your own templates. 

If that's the case, you can list the templates in the custom index by running:
```shell
create_app list --index="https://www.somewhere.com/templates-index"
```

And create your project from a template in that index:
```shell
create_app create TEMPLATE_NAME --index="https://www.somewhere.com/templates-index"
```


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
