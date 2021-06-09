import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deathdaily",
    version="0.0.2",
    author="yoshiyasu takefuji",
    author_email="takefuji@keio.jp",
    description="A package for predicting the number of daily deaths",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ytakefuji/covid-19_daily_death_prediction",
    project_urls={
        "Bug Tracker": "https://github.com/ytakefuji/covid-19_daily_death_prediction",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['deathdaily'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    entry_points = {
        'console_scripts': [
            'deathdaily = deathdaily:main'
        ]
    },
)
