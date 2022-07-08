from pathlib import Path

from setuptools import setup

from create_app.settings import (
    GIT_REPOSITORY,
    PACKAGE_NAME,
    PYPI_PACKAGE_NAME,
    REQUIREMENTS_FILE,
)

ROOT_PATH = Path(__file__).parent


VERSION = "0.1.2"


README_FILENAME = "README.md"


DESCRIPTION = (
    "A tool for creating applications from templates. Use your time wisely, "
    "while adopting state-of-the-art technologies and practices!"
)


ENTRY_POINTS = {
    "console_scripts": [f"{PACKAGE_NAME}={PACKAGE_NAME}.cli:main"],
}


def get_requirements():
    with open(REQUIREMENTS_FILE) as file:
        return file.readlines()


def get_long_description():
    (ROOT_PATH / README_FILENAME).read_text(encoding="utf8")


setup(
    name=PYPI_PACKAGE_NAME,
    entry_points=ENTRY_POINTS,
    version=VERSION,
    description=DESCRIPTION,
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    # keywords="", TODO
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        # "Development Status :: 5 - Production/Stable", TODO
        # "Operating System :: OS Independent", TODO
    ],
    url=GIT_REPOSITORY,
    author="Gabriel Bazan",
    author_email="gbazan@outlook.com",
    license="MIT",
    packages=[PACKAGE_NAME],
    zip_safe=False,
    python_requires=">=3.6.2",
    install_requires=get_requirements(),
)
