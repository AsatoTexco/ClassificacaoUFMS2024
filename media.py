import csv
 


def calc_media(notas):
    vL = 500 + 100 (notas[0] - 12.7926 )/4.9462
    vH = 500 + 100 (notas[1] - 14.8008)/4.7836
    vN = 500 + 100 (notas[2] - 13.5814)/5.0906
    vM = 500 + 100 (notas[3] - 12.1816)/5.8015
    r = notas[4]
    
    pR = 2
    pH = 1
    pN = 1
    pL = 2
    pM = 2
    
    nF = (pR * r + pH * vH + pN * vN + pL * vL + pM * vM) / (pR + pH + pN + pL + pM )
    
    return nF 

caminho_arquivo = 'candidatos_SI.csv'

 
concorrentes = {}
with open('candidatos_SI.csv', mode='r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    
    for linha in leitor_csv:
        concorrentes[linha[0]] = linha[1]
 