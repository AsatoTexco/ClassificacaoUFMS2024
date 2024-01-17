# Extrair os dados dos participantes dos respectivos cursos

import csv

def cad_conc(dados): 
    dados = dados.split('\n')
    conc = [] 
    for i in dados:
        if(i[0:6].isdigit()): 
            conc.append([i[0:6],i[7:25]]) 
            print(i)
    return conc
              
texto = ""
print("Digite seu texto (digite 'fim' em uma linha separada para encerrar):")
while True:
    linha = input()
    if linha.lower() == 'fim':
        break
    texto += linha + '\n'
 

concorrentes = cad_conc(texto) 
with open('./candidatos.csv', mode='w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv) 
    for c in concorrentes: 
        escritor_csv.writerow([c[0],c[1]])