import os
from get_project_root import root_path
from setuptools import setup, find_packages

# PATH VARIABLES
SOURCE_NAME = "src"
ROOT_DIR = root_path(ignore_cwd=True)
FRAMEWORK_NAME = os.path.basename(ROOT_DIR)
REQUIREMENTS_FILE = os.path.join(ROOT_DIR, "requirements.txt")
PATH_TO_RESOURCES = os.path.join("core", "resources")

# PROJECT VARIABLES
CURRENT_VERSION = "0.3.3"
LICENSE_TYPE = "MIT"

# AUTHOR VARIABLES
AUTHOR_FULL_NAME = "Philip Vasilevsky"
AUTHOR_EMAIL = "fil13698@gmail.com"
LINK_TO_REPO = "https://github.com/philip136/PyWebUIFramework"

# PACKAGE VARIABLES
ALL_SOURCE_PACKAGES = find_packages(SOURCE_NAME)
DEPENDENCIES = []


if os.path.exists(REQUIREMENTS_FILE):
    with open(REQUIREMENTS_FILE) as req_file:
        DEPENDENCIES.extend([dep_name.strip("\n") for dep_name in req_file.readlines()])
else:
    raise FileNotFoundError("Requirements file has not been found")


setup(
    name=FRAMEWORK_NAME,
    version=CURRENT_VERSION,
    license=LICENSE_TYPE,
    author=AUTHOR_FULL_NAME,
    author_email=AUTHOR_EMAIL,
    packages=ALL_SOURCE_PACKAGES,
    package_dir={"": SOURCE_NAME},
    package_data={"": [PATH_TO_RESOURCES]},
    include_package_data=True,
    url=LINK_TO_REPO,
    keywords=FRAMEWORK_NAME,
    install_requires=DEPENDENCIES
)
