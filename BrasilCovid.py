import csv
with open('brasil_covid.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    next(leitor)
    for linha in leitor:
        if float(linha[2]) > 1:
            print(linha)

with open('Novo_Csv.csv', 'w', encoding='utf-8', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(['Nome', 'Idade', 'Email', 'Sexo'])
    escritor.writerow(['William', '27', 'william@email.com', 'Masculino'])

with open('Novo_Csv.csv', 'r', encoding='utf-8') as arquivo_csv:
    for linha in arquivo_csv:
        print(linha, end='')