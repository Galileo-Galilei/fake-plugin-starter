import pathlib

from setuptools import find_packages, setup

NAME = "fake_plugin_starter"
HERE = pathlib.Path(__file__).parent


setup(
    name=NAME,
    version="0.0.1",
    description="A fake kedro plugin to test starter injection functionnality",
    url="https://github.com/Galileo-Galilei/fake_plugin_starter",
    python_requires=">=3.6, <3.9",
    packages=find_packages(),
    author="Yolan Honoré-Rougé",
    entry_points={
        "kedro.starter": ["starter =  starter_constant:starters"],
    },
    keywords="kedro-plugin",
)
