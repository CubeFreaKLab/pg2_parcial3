#!/usr/bin/env python3
"""
Setup script for jorge_ch_pg2_tecba library
"""

from setuptools import setup, find_packages

# Read the requirements from requirements.txt
def read_requirements():
    """
    Lee las dependencias de runtime (no las de desarrollo).
    Para esta librería, no hay dependencias externas - solo usa módulos estándar.
    """
    # Tu librería solo usa 're' (regex) que es built-in, no necesita instalación
    return []

# Read the long description from README if it exists
def read_long_description():
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Una librería básica de validadores para datos personales y de contacto"

setup(
    name="jorge-choque-pg2-tecba",
    version="0.0.1",
    author="Jorge Daniel Choque Ferrufino",
    author_email="jorgechoque.sis24ch@tecba.edu.bo",
    description="Una librería básica de validadores para datos personales y de contacto",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/CubeFreaKLab/pg2_parcial3",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black",
            "flake8",
            "mypy",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="validators, validation, personal data, contact data",
    project_urls={
        "Bug Reports": "https://github.com/CubeFreaKLab/pg2_parcial3/issues",
        "Source": "https://github.com/CubeFreaKLab/pg2_parcial3",
    },
)