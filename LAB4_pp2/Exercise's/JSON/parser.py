import json
parseFile = open('lab4//JSON//db.json')

somevalue = json.load(parseFile)

print("Interface Status\n================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
for member in somevalue["imdata"]:
    print(member['l1PhysIf']['attributes']['dn'],"\t\t\t\t",member['l1PhysIf']['attributes']['speed']," ",member['l1PhysIf']['attributes']['mtu'])





#print(parseFile)
