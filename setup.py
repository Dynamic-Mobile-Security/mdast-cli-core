from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mdast_cli_core",
    version='2.1',
    author="Dynamic-Mobile-Security",
    description="mDast core package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dynamic-Mobile-Security/mdast-cli-core",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
         'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
)
