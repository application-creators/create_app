# Create App

_create_app_ is a tool for creating applications from templates. 

Everytime developers need to start a new project, they have to define and figure out things like: 
Which project structure to use, how to dockerize, run unit tests, check the code style, format the code,
add GIT hooks, among many others. _create_app_ is a tool that you can use to base your new project
from a template that provides all that, and more. This way you can quickly start making your idea 
come true, without reinventing the wheel: That means that you use your time wisely, while adopting 
state-of-the-art technologies and practices.


## Installation

Simply install it with PIP:
```shell
python -m pip install create_app
```

## Usage

Simply run this command to generate your project:
```shell
create_app [template_name]
```

Or:
```shell
python -m create_app [template_name]
```

If you don't provide the _template_name_ argument, it defaults to "python_simple".


## Index of Available Templates

There's an [official index of templates](/templates.json), from which you can get your project started:

| **Template name**              | **Description**                                                                                                                                | **Repo**                                                                     |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| python_simple                  | Simple Python project with Docker                                                                                                              | [Link](https://github.com/application-creators/python_simple)                |
| python_compose                 | Simple Python project with Docker Compose                                                                                                      | [Link](https://github.com/application-creators/python_compose)               |
| python_fastapi                 | FastAPI project with Docker                                                                                                                    | [Link](https://github.com/application-creators/python_fastapi)               |
| python_fastapi_with_database   | FastAPI project with Docker Compose and PostgreSQL (which can be very easily changed for any other engine), SQLAlchemy, and Alembic migrations | [Link](https://github.com/application-creators/python_fastapi_with_database) |

At the moment there are only Python templates available in the official index. But _create_app_ can 
generate applications of literally **any language**.


## Contribute

[Application Creators](https://github.com/application-creators) is a new GitHub organization I've created
to host, debate, and maintain this tool and all the official templates. It is the idea to generate state-of-the-art
templates which are useful to everyone. Feel free to express you opinion and contribute!
