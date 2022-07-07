from os.path import basename, dirname

TEST_MODULE_SUFFIX = "_test.py"
MODULES_SEPARATOR = "."


def get_package_name(test_file):
    path = dirname(test_file)
    tests_path = dirname(path)
    package_name = basename(tests_path)
    return package_name


def get_module_name(test_file):
    test_module_name = basename(test_file)
    return test_module_name.replace(TEST_MODULE_SUFFIX, "")


def get_module(test_file):
    package_name = get_package_name(test_file)
    module_name = get_module_name(test_file)
    return f"{package_name}{MODULES_SEPARATOR}{module_name}"
