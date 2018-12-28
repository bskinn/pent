import re
from setuptools import setup

from pent import __version__


NAME = "pent"


def readme():
    with open("README.rst", "r") as f:
        content = f.read()

    # Helper function
    def content_update(content, pattern, sub):
        return re.sub(pattern, sub, content, flags=re.M | re.I)

    # Docs reference updates to current release version, for PyPI
    # This one gets the badge image
    content = content_update(
        content,
        r"(?<=/readthedocs/{0}/)\S+?(?=\.svg$)".format(NAME),
        "v" + __version__,
    )

    # This one gets the RtD links
    content = content_update(
        content,
        r"(?<={0}\.readthedocs\.io/en/)\S+?(?=[/>])".format(NAME),
        "v" + __version__,
    )

    return content


setup(
    name="pent",
    version=__version__,
    description="pent Extracts Numerical Text",
    long_description=readme(),
    url="https://www.github.com/bskinn/pent",
    license="MIT License",
    author="Brian Skinn",
    author_email="bskinn@alum.mit.edu",
    packages=["pent"],
    provides=["pent"],
    python_requires=">=3.4",
    requires=["attrs (>=17.1)", "pyparsing (>=1.5.5)"],
    install_requires=["attrs>=17.1", "pyparsing>=1.5.5"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Utilities",
        "Development Status :: 3 - Alpha",
    ],
)
