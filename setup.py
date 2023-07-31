import os
from string import Template

try:
    from skbuild import setup  # This line replaces 'from setuptools import setup'
except ModuleNotFoundError:
    # use classical setuptools to build sdist
    from setuptools import setup

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "python" / "README.md").read_text()

MAJOR_VERSION = 0
MINOR_VERSION = 2
PATCH_VERSION = 0

PACKAGE_NAME = "drift-bytes"

VERSION_SUFFIX = os.getenv("VERSION_SUFFIX")


def update_package_version(path: Path, version: str, protoc_version: str):
    """Overwrite/create __init__.py file and fill __version__"""
    template = (path / "__init__.py.in").read_text(encoding="utf-8")
    init_content = Template(template).substitute(
        version=version, protoc_version=protoc_version
    )
    with open(path / "__init__.py", "w") as f:
        f.write(init_content)


def build_version():
    """Build dynamic version and update version in package"""
    version = f"{MAJOR_VERSION}.{MINOR_VERSION}.{PATCH_VERSION}"
    if VERSION_SUFFIX:
        version += f"dev.{VERSION_SUFFIX}"

    return version


setup(
    name=PACKAGE_NAME,
    version=build_version(),
    packages=["drift_bytes"],
    package_dir={"": "python/src"},
    cmake_install_dir="python/src/drift_bytes",
    cmake_source_dir="python",
    author="PANDA, GmbH",
    author_email="info@panda.technology",
    description="A serializer for typed data in the Drift infrastructure.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/panda-official/DriftBytes",
    python_requires=">=3.8",
    license="MPL-2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
    ],
)
