with open("Teste.txt", "r") as arquivo:
    conteudo=arquivo.readlines()
print("tipo da variavel", type(conteudo))
print("Conteudo do arquivo: ", conteudo)