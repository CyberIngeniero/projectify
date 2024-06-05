from setuptools import find_packages, setup

setup(
    name="Projectify",
    version="0.1.0",
    description="A tool to set up a Python project structure",
    author="CyberIngeniero",
    author_email="npinoa.ai@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "colorama",
        "art",
        "packaging",
    ],
    entry_points={
        "console_scripts": [
            "setup_proyect=projectify.core:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
