import requests,json
from random import randint
class random():
    def anime(source=False, min="1", max=False, check=True):
        if source == False:
            if not check:
                return f"http://neko-bot.net/anime/anime{str(randint(int(min), int(str(requests.get('http://neko-bot.net/info/totalanime.txt').text))))}.png"
            if check is True:
                while True:
                    total=requests.get('http://neko-bot.net/info/totalanime.txt').text
                    num = str(randint(int(min), int(total)))
                    sources = json.loads(requests.get('http://neko-bot.net/info/anime.json').text)[f'{num}']
                    #print(sources)
                    if sources is "":
                        pass
                    if sources is not "":
                        break
                        # sources = json.loads(requests.get('http://neko-bot.net/info/anime.json').text)
            # animeNum = str(randint(int(min), int(total)))
            out = f"http://neko-bot.net/anime/{num}.png"
            return out
        if source == True:

            if max == False:
                total = requests.get('http://neko-bot.net/info/totalanime.txt').text
            if max is not False:
                total = max
            if not check:
                num=f"{str(randint(int(min), int(str(requests.get('http://neko-bot.net/info/totalanime.txt').text))))}"

            if check is True:
                while True:
                    num = str(randint(int(min), int(total)))
                    sources = json.loads(requests.get('http://neko-bot.net/info/anime.json').text)[f'{num}']
                    #print(sources)
                    if sources is "":
                        pass
                    if sources is not "":
                        break
                        # sources = json.loads(requests.get('http://neko-bot.net/info/anime.json').text)
            # animeNum = str(randint(int(min), int(total)))
            out = f"http://neko-bot.net/anime/{num}.png"
            # animeSource = sources[f"{animeNum}"]
            output = {"url": out, "source": sources, 'ID': str(num)}

            return dict(output)

    def neko(source=False, min='1', max=False, check=True):

        if source == False:
            if not check:
                output = f"http://neko-bot.net/nekos/neko{str(randint(int(min), int(str(requests.get('http://neko-bot.net/info/totalnekos.txt').text))))}.png"
                return output
            if check is True:
                while True:
                    total=requests.get('http://neko-bot.net/info/totalanime.txt').text
                    num = str(randint(int(min), int(total)))
                    sources = json.loads(requests.get('http://neko-bot.net/info/nekos.json').text)[f'{num}']
                    #print(sources)
                    if sources is "":
                        pass
                    if sources is not "":
                        break
                        # sources = json.loads(requests.get('http://neko-bot.net/info/anime.json').text)
            # animeNum = str(randint(int(min), int(total)))
            out = f"http://neko-bot.net/nekos/{num}.png"
            return out
        if source == True:
            if max == False:
                total = requests.get('http://neko-bot.net/info/totalnekos.txt').text
            if max is not False:
                total = max
            if check is True:
                while True:
                    num = str(randint(int(min), int(total)))
                    sources = json.loads(requests.get('http://neko-bot.net/info/nekos.json').text)[f'{num}']
                    #print(sources)
                    if sources is "":
                        pass
                    if sources is not "":
                        break
                        # sources = json.loads(requests.get('http://neko-bot.net/info/anime.json').text)
            # animeNum = str(randint(int(min), int(total)))
            out = f"http://neko-bot.net/nekos/{num}.png"
            # animeSource = sources[f"{animeNum}"]
            output = {"url": out, "source": sources, 'ID': str(num)}


            return dict(output)

    class pat():
        def static():
            return f"http://neko-bot.net/pats/static/{str(randint(int(1), int(str(requests.get('http://neko-bot.net/info/totalpats.txt').text))))}.png"

        def animated():
            return f"http://neko-bot.net/pats/animated/{str(randint(int(1), int(str(requests.get('http://neko-bot.net/info/totalpats_a.txt').text))))}.png"

    class hug():
        def animated():
            return "This endpoint is not finished!"

        def static():
            return "This endpoint is not finished!"

