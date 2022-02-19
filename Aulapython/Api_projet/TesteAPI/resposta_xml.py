# -*- coding: utf-8 -*-
from email import charset
import os

import sys

sys.maxsize

# abrir arquivo de log
resposta = open('arquivo.xml', 'w')
# gravar = input("Insira o response\n\n")
print("Insira o response .xml: \n\n")
lines = []
while True:
    line = str(input())
    if line:
        # print(len(line))
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
resposta.write(text)
resposta.close()
