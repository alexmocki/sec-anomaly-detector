from setuptools import setup

setup(
    name="secad",
    version="0.1",
    py_modules=["main"],
    entry_points={
        "console_scripts": [
            "secad=main:main"
        ]
    },
)
