import fitz  # PyMuPDF
import csv 

# função para calcular média 
def calc_media(notas):
    
    if(len(notas) > 1): 
        
        # definindo notas 
        vL = float(notas[0].replace(',','.'))
        vH = float(notas[1].replace(',','.'))
        vN = float(notas[2].replace(',','.'))
        vM = float(notas[3].replace(',','.'))
        r = float(notas[4].replace(',','.'))
        
        # pesos das disciplinas 
        pR = 2
        pH = 1
        pN = 1
        pL = 2
        pM = 2
        
        # calculo do edital :)
        nF = (pR * r + pH * vH + pN * vN + pL * vL + pM * vM) / (pR + pH + pN + pL + pM )
        return nF
    
    # retorna 100 se não tiver as notas 
    return 100 

def get_concorrentes():
    
    # analisando arquivo de concorrentes 
    concorrentes = {}
    with open('candidatos_SI.csv', mode='r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        
        for linha in leitor_csv:
            concorrentes[linha[0]] = linha[1] 
            
    return concorrentes


# função extrair todos os dados de todos os participantes e criar um dict 
def extrair_todas_tabelas_pdf(caminho_pdf):
    dados = {} 
    
    with fitz.open(caminho_pdf) as documento_pdf:
        for pagina_numero in range(documento_pdf.page_count):
            pagina = documento_pdf[pagina_numero]
            blocos = pagina.get_text("blocks")
               
            for bloco in blocos:
                if (bloco[4].split('\n')[0].isdigit()):   
                    dados_pessoa = bloco[4].split('\n')  
                    dados[dados_pessoa[0]] = [dados_pessoa[1], dados_pessoa[2].split(' ')]      
                         
    return dados
 
caminho_pdf = 'notas_participantes.pdf'
dados_pdf = extrair_todas_tabelas_pdf(caminho_pdf)
concorrentes = get_concorrentes()

colocacao = {}

for i in concorrentes:
    colocacao[i] = [concorrentes[i], calc_media(dados_pdf[i][1])]
    
colocacao_ordenada = dict(sorted(colocacao.items(),key=lambda x: x[1][1],reverse=True))

position = 1
for i in colocacao_ordenada:
    if(dados_pdf[i][0] == "AC"):
        
        print(f'{position}° - {colocacao_ordenada[i][0]} - {colocacao_ordenada[i][1]} - {dados_pdf[i][0]}')
        position+=1 