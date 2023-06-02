import os
from setuptools import setup, find_packages
import pkutils

# PATH VARIABLES
SOURCE_NAME = "src"
FRAMEWORK_NAME = "PyWebUIFramework"
PATH_TO_RESOURCES = os.path.join("core", "resources")

# PROJECT VARIABLES
CURRENT_VERSION = "1.6"
LICENSE_TYPE = "MIT"

# AUTHOR VARIABLES
AUTHOR_FULL_NAME = "Philip Vasilevsky"
AUTHOR_EMAIL = "fil13698@gmail.com"
LINK_TO_REPO = "https://github.com/philip136/PyWebUIFramework"

# PACKAGE VARIABLES
ALL_SOURCE_PACKAGES = find_packages(SOURCE_NAME)
DEPENDENCIES = list(pkutils.parse_requirements("requirements.txt"))


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
