import requests
import datetime
import json


dt_now = datetime.datetime.now()

uri = 'https://livlog.xyz/hoshimiru/planet'
params={'lat': 35.6581, 'lng': 139.7414, 'date': datetime.date.today(), 'hour': dt_now.hour, 'min': dt_now.min}

res = requests.get(uri, params)
jres = json.dumps(json.loads(res.text), indent=4)
lst = res.json()["result"]


def title():
    return "\n\t-* above the star *-\n"


def alt():
    return lst[i]["altitudeNum"] < 0
   

class Content:
    def __init__(self,nm,al,di,im):
        self.nm = nm
        self.al = al
        self.di = di
        self.im = im

    def details(num):
        star = lst[int(num)]
        nm = "\n Name:       " + star["enName"] + "\n"
        al = "Altitude:   " + str(star["altitudeNum"]) + "\n"
        di = "Direction:  " + str(star["directionNum"]) + "\n"
        im = "Star image: " + star["starImage"]
        return Content(nm, al, di, im)


print(title())
print("  The stars twinkle above your head!\n")

for i in range(len(lst)):
    if alt():
        continue
    else:
        print(i, lst[i]["enName"])

while True:
    want = "\nDo you want to know the detailed information?\ny(es) or n(o) -->"
    if input(want) == 'n': break
    num = "\nplease, enter the number that you want to know  -->"
    cont = Content.details(input(num))
    print(cont.nm, cont.al, cont.di, cont.im)

print("\nHave a nice day!")
        

