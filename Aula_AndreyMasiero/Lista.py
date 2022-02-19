lista= ['a','b','c']
lista[2] ='e'
print(lista)

print("===========Add. informações na lista")
cliente=[]
cliente.append('Ana')
print(cliente)
cliente.append('Paulo')
print(cliente)
print("=========item na lista com insert======")

cliente.insert(0, 'Marta')
print(cliente)
print("=========remover objeto======")
cliente.remove('Ana')
print(cliente)
print("=========remover o ultimo objeto======")
cliente.pop()
print(cliente)
print("===========Add. informações na lista")
cliente.append('Jose')
print(cliente)
print("===========Add. informações na lista")
cliente.append('Gabriel')
print(cliente)

print("=====================juntando listas=====================")

lista =['Gloria', 'Jose', 'Gabriel', 'Tulio']
lista2= ['Marta', 'Ana', 'Paulo']

lista.extend(lista2)
print(lista)

print("===========indice de um valor==========")
lista.index('Tulio')


#print(lista[0])

print("=========== Contar indice da lista==========")
lista.count('Tulio')


print("=========== Ordenar lista==========")
lista.sort()
print(lista)



