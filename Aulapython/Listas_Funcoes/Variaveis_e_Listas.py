inventario=[]
resposta="S"
while resposta=="S":
    inventario.append(input("Equipamento:"))
    inventario.append(float (input("Valor: ")))
    inventario.append(int(input("Numero Serial: ")))
    inventario.append(input("Departamento: "))
    resposta=input("Se desejar continuar, digite \"S\"  ").upper()

    for elemento in inventario:
        print(elemento)
