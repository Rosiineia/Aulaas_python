usuarios={}
print(usuarios)

usuarios= {"Chaves":["Chaves Silva","17/06/2017","Recep_01"],
    "Quico":["Enrico Flores","03/06/2017","Raiox_02"]
    }

print(usuarios)

usuarios["Florinda"]= ["Dona Florinda Silva","17/06/2015","Recep_01"]
print(usuarios)

print("###############################")
print(usuarios.get("Florinda"))
print(usuarios.get("Chaves"))
 
