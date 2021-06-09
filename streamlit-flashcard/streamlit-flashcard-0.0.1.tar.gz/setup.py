import setuptools

setuptools.setup(
    name="streamlit-flashcard",
    version="0.0.1",
    author="Leejay Xia",
    author_email="leejayxia@gmail.com",
    description="Custom flash card component for streamlit",
    long_description="Responsive and customizable flash card component for streamlit",
    long_description_content_type="text/plain",
    url="https://scout.cool",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
