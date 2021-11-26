from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mdast_cli_core",
    version='2.5',
    author="Dynamic-Mobile-Security",
    description="mDast core package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dynamic-Mobile-Security/mdast-cli-core",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
         'requests > 2.20'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
)
