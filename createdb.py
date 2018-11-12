import mysql.connector as mariadb
import json


dbs_host = "localhost"
dbs_user = "root"
dbs_password = "123456"

dbName = "waifus"

pasada=0

def createDb2Query(dic, tableName):
    query = "CREATE TABLE IF NOT EXISTS " + tableName + " ("
    keys = list(dic.keys())
    query+=keys[0] + " " + sqltypes[type(dic[keys[0]]).__name__] + " PRIMARY KEY"
    for k in keys[1:]:
        query+=", " + k + " " + sqltypes[type(dic[k]).__name__]
    query+=")"
        
    return query

sqltypes = {
        'int': 'int',
        'str': 'longtext',
        'NoneType': 'varchar(10000)', 
        'dict': 'longtext',
        'list': 'longtext'
}

def insert2DbQuery(valW, valS, valC, valT, rows):
    sqlW= "INSERT IGNORE INTO waifus "+ str(tuple(rows[0].keys())).replace("'", '') + " VALUES (%s"
    for t in range(len(tuple(rows[0].keys()))-1):
        sqlW+=", %s"
    sqlW+=")"
    print("ok")
        
    sqlS= "INSERT IGNORE INTO series "+ str(tuple(rows[0]['series'].keys())).replace("'", '') + " VALUES (%s"
    for t in range(len(tuple(rows[0]['series'].keys()))-1):
        sqlS+=", %s"
    sqlS+=")"
    print("ok")
        
    sqlC= "INSERT IGNORE INTO creators "+ str(tuple(rows[0]['creator'].keys())).replace("'", '') + " VALUES (%s"
    for t in range(len(tuple(rows[0]['creator'].keys()))-1):
        sqlC+=", %s"
    sqlC+=")"
    print("ok")
        
    sqlT= "INSERT IGNORE INTO tags (id, name) VALUES (%s, %s)"
    print("ok")
        
    print(sqlW)
#    print(sqlS)
#    print(sqlC)
#    print(sqlT)
        

    for r in rows:
        t=()
        tuplasSer=()
        tuplasCre=()
        for k in list(r.keys()):
            if type(r[k]).__name__ == 'NoneType':
                if k =='age' or k == 'birthday_day':
                    t+=(-1,)
                else:
                    t+=("",)
            elif type(r[k]).__name__ == 'dict':
                t+=(r[k]['id'],)
            elif type(r[k]).__name__ == 'list':
                t+=(str(r[k]),)
            else:
                t+=(r[k],)
            if k == 'series':
                for sk in list(r[k].keys()):
                    if type(r[k]).__name__ == 'NoneType':
                        tuplasSer+=("NULL",)
                    else:
                        tuplasSer+=(r[k][sk],)
            elif k == 'creator':
                if type(r[k]).__name__ == 'NoneType':
                    tuplasCre+=(-1, 'Unknown', 'Unknown')
                else:
                    for ck in list(r[k].keys()):
                        if type(r[k]).__name__ == 'NoneType':
                            tuplasCre+=("NULL",)
                        else:
                            tuplasCre+=((r[k][ck]),)
            elif k == 'tags':
                for tk in r[k]:
                    tuplasTag=()
                    tuplasTag+=((tk['id']),)
                    tuplasTag+=((tk['name']),)
                    valT.append(tuplasTag)
#            print(k)
        global pasada
        print("pasada: " + str(pasada))   
        pasada+=1
        valW.append(t)
        valS.append(tuplasSer)
        valC.append(tuplasCre)

    return sqlW, sqlS, sqlC, sqlT

def createTables(cursor, rows):
    valW=[]
    valS=[]
    valC=[]
    valT=[]    
    sqlW, sqlS, sqlC, sqlT = insert2DbQuery(valW, valS, valC, valT, rows)
    
    print("ok")
    cursor.executemany(sqlW, valW)
    print("ok")
    cursor.executemany(sqlS, valS)
    print("ok")
    cursor.executemany(sqlC, valC)
    print("ok")
    print("osk")
    print(valT[1])
    cursor.executemany(sqlT, valT)
    print("ok")
            

try:
    dbs = mariadb.connect(
        host=dbs_host,
        user=dbs_user,
        password=dbs_password
    )
    cursor = dbs.cursor()
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS "+dbName)
    cursor.execute("USE "+dbName)

    with open('waifus.json') as json_data:
        rows = json.load(json_data)
    
    cursor.execute(createDb2Query(rows[0], 'waifus'))
    cursor.execute(createDb2Query(rows[0]['series'], 'series'))
    cursor.execute(createDb2Query(rows[0]['creator'], 'creators'))
    cursor.execute(createDb2Query(rows[0]['tags'][0], 'tags'))

    createTables(cursor, rows)
    
    dbs.commit()
    print(cursor.rowcount, "was inserted.")
    
    
except mariadb.Error as error:
    print("Error: "+error.msg)
