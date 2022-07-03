from setuptools import setup

PYPI_PACKAGE_NAME = "create_py_app"
PACKAGE_NAME = "create_python_app"
REQUIREMENTS_FILE = "requirements.frozen"


ENTRY_POINTS = {
    "console_scripts": [f"{PACKAGE_NAME}={PACKAGE_NAME}.cli:main"],
}


def get_requirements():
    with open(REQUIREMENTS_FILE) as file:
        return file.readlines()


setup(
    name=PYPI_PACKAGE_NAME,
    entry_points=ENTRY_POINTS,
    version="0.1",
    description="CLI to create new Python applications",
    url="https://github.com/gabrielbazan/create_python_app",
    author="Gabriel Bazan",
    author_email="gbazan@outlook.com",
    license="MIT",
    packages=[PACKAGE_NAME],
    zip_safe=False,
    python_requires=">=3.6.2",
    install_requires=get_requirements(),
)
