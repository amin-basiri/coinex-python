import setuptools

with open("requirements/base.txt", "r", encoding="utf-8") as fh:
    requirements = fh.readlines()


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="coinex-python",
    version="0.1.0",
    author="Amin Basiri",
    author_email="amin.bsr99@gmail.com",
    description="Python package to use Coinex cryptocurrency exchange API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amin-basiri/coinex-python",
    project_urls={
        "Bug Tracker": "https://github.com/amin-basiri/coinex-python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*"]
    ),
    install_requires=[req for req in requirements],
    python_requires=">=3.6",
    include_package_data=True,
)
