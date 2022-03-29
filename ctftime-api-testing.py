import requests as r
url = "https://ctftime.org/api/v1/events/?limit=100&start=1422019499&finish=1423029499"
apires = r.get(url)
var1 = apires.json()[0]

