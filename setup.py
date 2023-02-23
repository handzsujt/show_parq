from setuptools import setup

# to install with pipx first build with python setup.py bdist_wheel

setup(
    name="show-parquet",
    version="0.0.1",
    py_modules=["show_parq"],
    install_requires=["pandas", "pyarrow", "pandastable"],
    entry_points={
        "console_scripts": [
            "show-parquet = show_parq:main",
        ]
    },
)
