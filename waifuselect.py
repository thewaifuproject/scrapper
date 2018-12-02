import json, os, random

waifus2select=450

waifus = json.loads(open("waifus.json").read())

waifus=sorted(waifus, key=lambda w: w["likes"]+w["trash"])[-waifus2select:]

random.shuffle(waifus)

os.system("rm ../server/image/*")
for i, w in enumerate(waifus):
    newId=i
    imgName=w['display_picture'].split('/')[-1]
    os.system("cp images/"+imgName+" ../server/image/"+imgName)
    waifus[i]["id"]=newId
    waifus[i]["display_picture"]="https://api.waifuchain.moe/image/"+imgName

open("final/waifus.json", "w+").write(json.dumps(waifus))
