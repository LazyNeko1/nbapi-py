from . import rimg as RIMG
from . import apil as APIL
from . import simg as SIMG
from random import randint
class random:
    def anime(source=False, min="1", max=False, check=True):
        out = RIMG.random.anime(source=source,min=min,max=max,check=check)

        return out
    def neko(source=False, min="1", max=False, check=True):
        out = RIMG.random.anime(source=source,min=min,max=max,check=check)

        return out
    class pat:
        def static():
            return RIMG.random.pat.static()
        def animated():
            return RIMG.random.pat.animated()
    class hug:
        def static():
            return RIMG.random.hug.static()
        def animated():
            return RIMG.random.hug.animated()
class search:
    def anime(num, source=False):
        out = SIMG.search.anime(num=num,source=source)

        return out
    def neko(num, source=False):
        out = SIMG.search.neko(num,source=source)

        return out

# Note: Using this API you are going to be using a API that MAY (unlikely) But MAY send NSFW results.
# If that happens, DM my owner (LazyNeko#5644), or join the Neko Support Server from the website.
#                   #-------------------------------------------------#
#                       To join: Copy the below link.  
#                       https://discord.gg/RauzUYK
#                   #--------------------------------------------------#
# You may edit this code to your needs. I dont mind ;3
# TODO: make requests smaller (DONE)
# TODO: make "hug"&"pat" animated&static endpoint! (DONE)
# TODO: make all endpoints seperate files (DONE, WIP1)





#print(search.neko(randint(1,10),True)) #DEBUG 2 (SEARCH WITH SOURCE)
#print(random.anime()) #CHECK FOR SOURCE-ONLY!


def version():
    return str(open("version.txt", "r").read())


