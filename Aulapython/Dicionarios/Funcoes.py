def perguntar():
    return input("O que deseja Realizar?\n "+
            "<I> - Para inserir um usuario\n"+
            "<P> - Para Pesquisar um usuario\n"+
            "<E> - Para Excluir um usuario\n"+
            "<L> - Para Listar um usuario\n").upper()
def inserir(dicionario):
   dicionario[input("Digite o login: ").upper()]= [input("Digite o Nome: ").upper(),
            input("Digite a ultima Data de acesso: "),
            input("Digite a ultima estação acessada: ").upper()]

   