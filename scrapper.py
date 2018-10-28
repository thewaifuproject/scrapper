import requests, json

final=17268

waifuId=17265
waifus=[]
while True:
    r=requests.get("https://mywaifulist.moe/api/waifu/"+str(waifuId), headers={'x-requested-with': 'XMLHttpRequest'})
    if (r.text==""):
        break;
    waifu=r.json()
    print("Scrapped "+waifu["name"])
    waifus.append(waifu)
    waifuId+=1
open("waifus.json", "w+").write(json.dumps(waifus))
