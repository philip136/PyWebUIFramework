import os
from setuptools import setup, find_packages

# PATH VARIABLES
SOURCE_NAME = "src"
FRAMEWORK_NAME = "PyWebUIFramework"
PATH_TO_RESOURCES = os.path.join(SOURCE_NAME, "core", "resources.*")

# PROJECT VARIABLES
CURRENT_VERSION = "2.5"
LICENSE_TYPE = "MIT"

# AUTHOR VARIABLES
AUTHOR_FULL_NAME = "Philip Vasilevsky"
AUTHOR_EMAIL = "fil13698@gmail.com"
LINK_TO_REPO = "https://github.com/philip136/PyWebUIFramework"

# PACKAGE VARIABLES
ALL_SOURCE_PACKAGES = find_packages(SOURCE_NAME)


setup(
    name=FRAMEWORK_NAME,
    version=CURRENT_VERSION,
    license=LICENSE_TYPE,
    author=AUTHOR_FULL_NAME,
    author_email=AUTHOR_EMAIL,
    packages=ALL_SOURCE_PACKAGES,
    package_dir={"": SOURCE_NAME},
    include_package_data=True,
    url=LINK_TO_REPO,
    keywords=FRAMEWORK_NAME,
    install_requires=[
        'flake8==3.9.2',
        'injector==0.18.4',
        'jsonpath-ng==1.5.3',
        'loguru==0.5.3',
        'selenium==4.9.1',
        'typing-extensions==3.10.0.2',
        'webdriver-manager==3.8.6',
        'urllib3==1.26.6',
        'get-project-root==0.2'
    ]
)
