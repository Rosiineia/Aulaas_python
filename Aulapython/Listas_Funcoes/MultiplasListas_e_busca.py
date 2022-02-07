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

    busca=input("\nDigite o nome do Equipamento que deseja buscar: ")
    for indice in range (0, len(equipamentos)):
     if busca==equipamentos[indice]:
        print("Valor.......", valores[indice])
        print("Serial.......", seriais[indice])
       

