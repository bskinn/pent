from setuptools import setup


def readme():
    with open("README.rst", "r") as f:
        return f.read()


setup(
    name="pent",
    version="0.0",
    packages=["pent"],
    url="https://www.github.com/bskinn/pent",
    license="MIT License",
    author="Brian Skinn",
    author_email="bskinn@alum.mit.edu",
    description="Pent Extracts Numerical Text",
    long_description=readme(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Utilities",
        "Development Status :: 1 - Planning",
    ],
)
