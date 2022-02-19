inventario={}
opcao=int(input("Digite:\n "
                "<1> para registrar ativo \n"
                "<2> para registrar arquivo \n"
                "<3> para exibir ativos armazenados \n"))
while opcao>0 and opcao<4:
    if opcao==1:
        resp="S"
while resp=="S":
    inventario[input("Digite o numero patrimonial: \n")]=[
        input("Digite da ultim atualização: \n"),
        input("Digite a descrição\n"),
        input("Digite o departamento \n")]
    resp=input("Digite <S> para continuar \n").upper()
if opcao==2:
    with open("inventario.csv", "a")  as inv:
        for chave, valor in inventario.items():
            inv.write(chave + ";" + valor[0] + ";" +
                      valor[1] + ";" + valor[2] + " ")
            print("Persistido com sucesso")
elif opcao==3:
    with open("inventario.csv", "r") as inv:
        print(inv.readlines())
        opcao=int(input("Digite "
                       "<1> para registrar ativo \n"
                        "<2> para registrar arquivo \n"
                        "<3> para exibier ativos armazenados \n"))


