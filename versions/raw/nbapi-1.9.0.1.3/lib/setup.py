import setuptools
from textwrap import wrap
def NewVersion():
    f = open("nbapi/version.txt","r+")
    v1 = str(f.read()).replace(".","")
    temp = str(int(v1) + 1)
    temp1 = wrap(temp,1)
    print(temp1)
    out = ".".join(temp1)
    f.seek(0)
    f.truncate()
    f.write(out)
    f.close()
    print(out)
    
    



NewVersion()
long_description = "Simple Anime API package"
versionF=open("nbapi/version.txt","r").read()
setuptools.setup(
    name="nbapi",
    version=versionF,
    author="LazyNeko",
    author_email="nekobot.help@gmail.com",
    description="A small API for anime/nekos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LazyNeko1/nbapi",
    #packages="nbapi",
    install_requires=['aiohttp','requests','asyncio'],
    package_data={
        'nbapi':['*.py']
    },
    py_modules=['nbapi/__init__'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
