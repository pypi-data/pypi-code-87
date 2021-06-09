import setuptools
from pathlib import Path

setuptools.setup(
    name="SarthakPDF",
    version=1.0,
    long_description=Path("README.md").read_text(),
    pacages=setuptools.find_packages(exclude=["tests", "data"])
)
