import json, os

waifus2select=400

waifus = json.loads(open("waifus.json").read())

waifus=sorted(waifus, key=lambda w: w["likes"]+w["trash"])[:waifus2select]

open("final/waifus.json", "w+").write(json.dumps(waifus))

for w in waifus:
    imageName=str(w["id"])
    os.system("mv images/"+imageName+" ../server/image/"+imageName)
