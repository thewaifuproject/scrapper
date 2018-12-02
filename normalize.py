import json, os

waifus = json.loads(open("waifus.json").read())

waifus=sorted(waifus, key=lambda w: w["likes"]+w["trash"])

for i, w in enumerate(waifus):
    newId=i
    extension=w['display_picture'].split('.')[-1]
    if(len(extension)>6):
        extension='jpeg' if extension[-4:]=='jpeg' else 'png'
    imgName=str(newId)+'.'+extension
    os.system("mv images/"+str(w["id"])+" images/"+imgName)
    waifus[i]["id"]=newId
    waifus[i]["display_picture"]="images/"+imgName

open("waifus.json", "w+").write(json.dumps(waifus))
