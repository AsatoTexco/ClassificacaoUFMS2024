# Classificação UFMS 2024 

Para todos os que aguardam ansiosamente a divulgação da classificação da UFMS para o curso de Sistemas de Informação em 2024, gostaria de apresentar um sistema que analisa todos os candidatos, proporcionando uma classificação precisa prévia.

# Funcionamento
Inicialmente, iniciei a seleção dos concorrentes para o curso de Sistemas de Informação por meio de um sistema personalizado que desenvolvi chamado `get_concorrentes.py`. Ao executar este script, você pode facilmente copiar e colar os dados dos candidatos no arquivo `edital_participantes.pdf` conforme exemplificado na imagem abaixo. Este processo simplifica a coleta de informações, tornando-o mais eficiente e amigável.

![imagem representativa](https://iili.io/JYrmSFS.png) 

Após inserir os dados de todos os concorrentes, o sistema irá gerar um arquivo `.csv` crucial para a elaboração das colocações. Vale ressaltar que já existe um arquivo disponível para o curso de Sistemas de Informação, pronto para ser utilizado nesse processo (`candidatos_SI.csv`).

![imagem representativa](https://iili.io/JYrps5X.png) 

Em seguida, você poderá executar o arquivo `classificacao.py`, o qual realiza a filtragem de todas as notas dos concorrentes para o curso de Sistemas de Informação. Como resultado, a classificação será apresentada de acordo com a média calculada pela função `calc_media`.

![imagem representativa](https://iili.io/JY490nj.png) 

Exemplo de saída(filtrando todos da vaga para Ampla concorrência - AC):

![imagem representativa](https://iili.io/JY4deou.png) 

# Obs
- Esse programa pode ser alterado e adptado para qualquer curso da UFMS ou outro edital similar
- O tipo de vaga também pode ser alterado na linha 72




