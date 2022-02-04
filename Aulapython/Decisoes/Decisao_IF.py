nome=input("Digite o nome: ")
idade=int(input("Digite a Idade: " ))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa? ").upper()
if idade>=65:
    print(("O Paciente " + nome + " POSSUI atendimento prioritario" ))
else:
    print(("O Paciente " + nome + " NÃO POSSUI atendimento prioritario"))