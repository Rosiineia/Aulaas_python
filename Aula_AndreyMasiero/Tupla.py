
print("============tupla========================")
#o valor da tupla (conjunto e valores declarado entre parenteses) é imutavel, erá o mesmo valor sempre

tupla = ('a','b','c','f','h','m')

print(tupla)

print("==========Consultar valores==========")

print(tupla.__getitem__(0))

print("==========Armazenar - registro===========")
coordenadas = (33.945, -118.408056)
latitude = coordenadas[0]
longitude = coordenadas[1]

descricao,tipo, valor = ('Alimentação', 'debito', 23.50)

#lista de tupla
alunos =[('Gloria Maria', 6.0),
    ('Maria Paula', 8.0),
    ('Manoel Gomes', 6.0),
    ('Marcos Gomes', 6.0)]


#Descaompactamento _Anderline descarta a variavel
for nome, _ in sorted(alunos): # unpacking
    print(nome)
print('===========buscar um item e agruopar o restante===============')
#buscar um item e agruopar o restante

a,b, *resto = range(7)#range: gera uma tupla
print(a)
print(b)
print(resto)

print("#posso movimentar o resto")

a, *resto, d, e = range(5)#range: gera uma tupla
print(a)
print(resto)
print(d)
print(e)

from collections import namedtuple
Aluno = namedtuple('Aluno',['nome', 'media'])

alunos = Aluno('Gloria', 6.5),('Manoel Gomes', 6.0),('Marcos Gomes', 6.0)

print(alunos)





