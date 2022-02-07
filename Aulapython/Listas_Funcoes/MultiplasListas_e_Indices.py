equipamentos=[]
valores=[]
seriais=[]
depatamentos =[]
resposta = "S"
while resposta =="S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Numero de serial: ")))
    depatamentos.append(input("Departamento: "))
    resposta= input("Digite \"S\" para continuar: ").upper()

    for indice in range (0, len(equipamentos)):
        print("\nEquipamento..: ",(indice+1))
        print("Nome.......: ", equipamentos[indice])
        print("Valor.......", valores[indice])
        print("Serial.......", seriais[indice])
        print("Departamentos .......", depatamentos[indice])

