# -*- coding: utf-8 -*-
from email import charset
import os

import sys

sys.maxsize

# abrir arquivo de log
resposta = open('arquivo.json','w')
#gravar = input("Insira o response\n\n")
print("Insira o response .json: \n\n")
lines = []
while True:
    line = str(input())
    if line:
        #print(len(line))
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
resposta.write(text)
resposta.close()
