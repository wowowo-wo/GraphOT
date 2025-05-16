from setuptools import setup, find_packages

setup(
    name="GraphOT",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "scipy",
        "networkx",
        "matplotlib",
    ],
    python_requires='>=3.7',
)