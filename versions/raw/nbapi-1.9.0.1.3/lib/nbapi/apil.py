import requests,json
class api():
    def locked(key, api_type):

        url = "http://api.neko-bot.net/api/locked/{api_type}"
        headers = {"TagKey": f"{key}"}
        r = requests.get(url=url, headers=headers)
        if "403" not in r.status_code:
            return r.text
        if "403" in r.status_code:
            print(f"Invalid token ({key}) was supplied.")
