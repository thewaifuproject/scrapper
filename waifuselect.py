import json, os, sha3

def keccak256(k):
    return int(sha3.keccak_256(k.encode()).hexdigest(), 16)

waifus2select=450

waifus = json.loads(open("waifus.json").read())

waifus=sorted(waifus, key=lambda w: w["likes"]+w["trash"])[-waifus2select:]

os.system("rm ../server/image/*")

for i, w in enumerate(waifus):
    newId=keccak256(w["name"])
    os.system("cp images/"+str(w["id"])+" ../server/image/"+str(newId))
    waifus[i]["id"]=newId
    waifus[i]["display_picture"]="https://api.waifuchain.moe/image/"+str(newId)

open("final/waifus.json", "w+").write(json.dumps(waifus))

waifuNames="pragma solidity ^0.4.24;\n\
\n\
contract WaifuNames{\n\
	//Total: 450 waifus\n\
        string[] waifusNames="+str(map(lambda w: w["name"].encode("utf-8"), waifus))+";\n\
}"

open("../contract/WaifuNames.sol", "w+").write(waifuNames)

