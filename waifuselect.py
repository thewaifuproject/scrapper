import json, os, random

waifus2select=450

waifus = json.loads(open("waifus.json").read())

waifus=sorted(waifus, key=lambda w: w["likes"]+w["trash"])[-waifus2select:]

random.shuffle(waifus)

os.system("rm ../server/image/*")
for i, w in enumerate(waifus):
    newId=i
    os.system("cp images/"+str(w["id"])+" ../server/image/"+str(newId))
    waifus[i]["id"]=newId
    waifus[i]["display_picture"]="https://api.waifuchain.moe/image/"+str(newId)

open("final/waifus.json", "w+").write(json.dumps(waifus))
