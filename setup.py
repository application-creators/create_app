from setuptools import setup

from create_app.settings import (
    GIT_REPOSITORY,
    PACKAGE_NAME,
    PYPI_PACKAGE_NAME,
    REQUIREMENTS_FILE,
)

ENTRY_POINTS = {
    "console_scripts": [f"{PACKAGE_NAME}={PACKAGE_NAME}.cli:main"],
}


def get_requirements():
    with open(REQUIREMENTS_FILE) as file:
        return file.readlines()


setup(
    name=PYPI_PACKAGE_NAME,
    entry_points=ENTRY_POINTS,
    version="0.1.2",
    description="CLI to create new Python applications",
    url=GIT_REPOSITORY,
    author="Gabriel Bazan",
    author_email="gbazan@outlook.com",
    license="MIT",
    packages=[PACKAGE_NAME],
    zip_safe=False,
    python_requires=">=3.6.2",
    install_requires=get_requirements(),
)
