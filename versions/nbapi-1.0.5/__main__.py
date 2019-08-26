import requests
from random import randint
class random():
    def anime():
        r = requests.get('http://neko-bot.net/info/totalanime.txt')                 
        animemax=r.text
        animemin=6
        total=randint(int(animemin),int(animemax))
        return 'http://neko-bot.net/anime/anime'+str(total)+'.png'
    def neko():
        r = requests.get('http://neko-bot.net/info/totalnekos.txt')                   
        nekomax=r.text
        nekomin=6
        total=randint(int(nekomin),int(nekomax))
        return 'http://neko-bot.net/nekos/neko'+str(total)+'.png'
