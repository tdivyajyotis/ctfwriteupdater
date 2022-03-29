import requests as r
url = "https://ctftime.org/api/v1/events/"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
}
params = {'limit': '100', 'start': '1646006400', 'finish': '1648588662'}
apires = r.get(url, headers=headers, params=params)
print(apires.json())

#credit for solving that api error ; nullctf's implementation of ctftime
#todo
#implement db or yml parser
#autobot to parse all events on ctftime