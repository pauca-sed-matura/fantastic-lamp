from setuptools import setup, find_packages

setup(
    name="toolbox",
    version="0.1",
    description="A Python toolbox for digital signal processing and ASCII data analysis",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "pandas",
        "matplotlib",
    ],
)
