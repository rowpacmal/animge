from setuptools import setup, find_packages

setup(
    name="animge",
    version="1.0",
    packages=find_packages(),  # finds your `app/` folder
    entry_points={
        "console_scripts": [
            "run=run:main",  # points to main() in run.py
        ],
    },
)
