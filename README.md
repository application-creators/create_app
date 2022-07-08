# Create App

_create_app_ is a tool for creating applications from templates.

When developers start a new project, they perform some repetitive tasks to build the basic project structure before 
actually start writing features. This basic structure involves things like: Well, the project structure, unit testing, 
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

| **Template name**              | **Description**                                                                                                                                | **Repo**                                                                     |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| python_simple                  | Simple Python project with Docker                                                                                                              | [Link](https://github.com/application-creators/python_simple)                |
| python_compose                 | Simple Python project with Docker Compose                                                                                                      | [Link](https://github.com/application-creators/python_compose)               |
| python_fastapi                 | FastAPI project with Docker                                                                                                                    | [Link](https://github.com/application-creators/python_fastapi)               |
| python_fastapi_with_database   | FastAPI project with Docker Compose and PostgreSQL (which can be very easily changed for any other engine), SQLAlchemy, and Alembic migrations | [Link](https://github.com/application-creators/python_fastapi_with_database) |


## Contribute

[Application Creators](https://github.com/application-creators) is a new GitHub organization I've created to host, 
debate, and maintain this tool and the project templates. Its goal is to generate state-of-the-art templates useful 
to everyone. Feel free to express you opinion and contribute!
