"""Setup script for the Africa project."""

from setuptools import setup, find_packages

setup(
    name="africa",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "reflex",
    ],
    author="Simon Graetz",
    author_email="simon.graetz@gmx.de",
    description="A full stack web app",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/simmihugs/miniature-octo-happiness",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD2 License",
        "Operating System :: Ubuntu24.04",
    ],
)
