

SYSTEM_PYTHON_BIN=python3

VIRTUALENV_PATH=./venv
VIRTUALENV_PYTHON_BIN=${VIRTUALENV_PATH}/bin/python3
VIRTUALENV_PIP_BIN=${VIRTUALENV_PATH}/bin/pip
VIRTUALENV_ACTIVATE=${VIRTUALENV_PATH}/bin/activate

REQUIREMENTS_FILE_PATH=./requirements.frozen
TEST_REQUIREMENTS_FILE_PATH=./requirements.test.frozen
BUILD_REQUIREMENTS_FILE_PATH=./requirements.build.frozen

SETUP_FILENAME=setup.py


install_git_hooks:
	pre-commit install


run_git_hooks:
	pre-commit run --all-files


cleanup:
	@echo "Cleaning up..."
	rm -fr *.egg-info
	rm -fr build
	rm -fr dist
	@echo "Done!"


create_virtualenv:
	@echo "Creating virtualenv..."
	${SYSTEM_PYTHON_BIN} -m venv "${VIRTUALENV_PATH}"
	@echo "Done!"


delete_virtualenv:
	@echo "Deleting virtualenv..."
	rm -fr ${VIRTUALENV_PATH}
	@echo "Done!"


install_requirements:
	@echo "Installing requirements..."
	${VIRTUALENV_PIP_BIN} install -r "${REQUIREMENTS_FILE_PATH}"
	@echo "Done!"


install_test_requirements:
	@echo "Installing test requirements..."
	${VIRTUALENV_PIP_BIN} install -r "${TEST_REQUIREMENTS_FILE_PATH}"
	@echo "Done!"


install_build_requirements:
	@echo "Installing build requirements..."
	${VIRTUALENV_PIP_BIN} install -r "${BUILD_REQUIREMENTS_FILE_PATH}"
	@echo "Done!"


install_all_requirements: install_requirements install_test_requirements install_build_requirements


run_unit_tests:
	@echo "Running unit tests..."
	. ${VIRTUALENV_ACTIVATE} && ./scripts/run_unit_tests.sh && deactivate
	@echo "Done!"


install_in_virtualenv:
	${VIRTUALENV_PIP_BIN} install -e .


build:
	${VIRTUALENV_PYTHON_BIN} -m build
