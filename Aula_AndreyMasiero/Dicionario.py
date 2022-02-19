#dicionario
alunos = {
    'Gloria Maria':('Gloria Maria', 10.0),
    'Maria Paula':('Maria Paula', 9.0),
    'Manoel Gomes':('Manoel Gomes', 7.0)
}
#buscar uma informação do dicionario

print(alunos.get('Manoel Gomes'))

print("===============================")

#retorna uma lista de tuplas
print(alunos.items())

print('============================')

#Associar chave a um valor

for key, value in alunos.items():
    print(f'Key: {key}==> Valor:{value}')

print("=========================")

#dicionario de chaves e valores

print(alunos.keys())
print(alunos.values())

print("==============================")
#Removendo valores

print(alunos.popitem()) #(remove o ultimo valor

print(alunos.pop('Maria Paula')) #remove um item especifico

print("======================")
#novo dicionario
novo_dic = alunos.copy()
print(novo_dic)
alunos.clear() #limpa dicionario

print("===========================================")
#criar novo dicionario

dicionario = dict([('chave','valor'),('chave2','valor2')])
print(dicionario)


