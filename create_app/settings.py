PACKAGE_NAME = "create_app"
PYPI_PACKAGE_NAME = "create_app"

GITHUB_USERNAME = "gabrielbazan"
GITHUB_PROJECT_NAME = "create_app"

GIT_REPOSITORY = f"https://github.com/{GITHUB_USERNAME}/{GITHUB_PROJECT_NAME}"


REQUIREMENTS_FILE = "requirements.frozen"


TEMPLATES_FILENAME = "templates.json"

TEMPLATES_FILE_BRANCH = "develop"  # TODO: Change to "main"

TEMPLATES_FILE_URI = (
    f"https://raw.githubusercontent.com/{GITHUB_USERNAME}"
    f"/{GITHUB_PROJECT_NAME}/{TEMPLATES_FILE_BRANCH}"
    f"/{PACKAGE_NAME}/{TEMPLATES_FILENAME}"
)


DEFAULT_TEMPLATE_NAME = "base"
