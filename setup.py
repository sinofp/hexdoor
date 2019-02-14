import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hexdoor",
    version="0.1.0",
    description="A colorful terminal hex viewer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sinofp/hexdoor",
    author="sinofp",
    license='WTFPL',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    keywords='hex viewer',
    packages=setuptools.find_packages(),
    install_requires=[
        'colorama',
        'fire'
    ],
    entry_points={
        'console_scripts': [
            'hexdoor=hexdoor.main:main',
        ],
    },
)