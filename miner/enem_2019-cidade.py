import pandas as pd
import numpy as np
import random

print("start")

cc = ';'
cidade = 'Belo Horizonte'
try:
    file  = open('../data/MICRODADOS_ENEM_2019.csv', 'rb')
    lines = file.readlines()
    count = 0
    number_lines = len(lines)
    print(number_lines)
except:
    print("erro leitura")

cols = str(lines[0]).split(';')
matrix = []

try:
    for i  in range(1,number_lines - 1):
        data_line = str(lines[i]).split(cc)
        municipio = str(data_line[80])
        if (municipio == cidade)  :
            matrix.append(data_line)
    data = np.array(matrix)
    df = pd.DataFrame(data=data, columns=cols)
    df.to_csv("../data/DADOS_ENEM_2019_SAMPLE_" + str(cidade) + ".csv", index=None)
except:
    print("erro leitura")

print("end")
