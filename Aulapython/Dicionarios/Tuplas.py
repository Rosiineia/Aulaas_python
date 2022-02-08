usuarios={}
emails = ["xpto@xyz.com","xkcd@phd.com"]

tuple = list(enumerate(emails))

for chave in range(0,len(tuple)):
    print("Email: ", tuple[chave][1])
    usuarios[tuple[chave]]=[input("Digite o nome: "), input("Digite o Nivel ")]

for chave, dado in usuarios.items():
    print("Usuarios..: ", chave[0])
    print("Email..: ", chave[1])
    print("Nome..: ", chave[0])
    print("Nivel..: ", chave[1])