import setuptools


long_description = (
"A small API for Anime, Nekos, etc."
)

setuptools.setup(
    name="nekobotapi",
    version="0.1.0",
    author="LazyNeko",
    author_email="nekobot.help.com",
    description="A Safe For Work anime API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LazyNeko1/nbapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
