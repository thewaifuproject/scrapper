import json, os, random

waifus2select=450

waifus = json.loads(open("waifus.json").read())

waifus=sorted(waifus, key=lambda w: w["likes"]+w["trash"])[-waifus2select:]

random.shuffle(waifus)

os.system("rm ../server/image/*")
for i, w in enumerate(waifus):
    newId=i
    extension=w['display_picture'].split('.')[-1]
    if(len(extension)>6):
        extension='jpeg' if extension[-4:]=='jpeg' else 'png'
    imgName=str(newId)+'.'+extension
    os.system("cp images/"+str(w["id"])+" ../server/image/"+imgName)
    waifus[i]["id"]=newId
    waifus[i]["display_picture"]="https://api.waifuchain.moe/image/"+imgName

open("final/waifus.json", "w+").write(json.dumps(waifus))
