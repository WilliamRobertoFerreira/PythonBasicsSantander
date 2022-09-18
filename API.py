import requests
url = 'https://open.er-api.com/v6/latest/USD'
req = requests.get(url)
dados = req.json()
diacotacao = dados['time_last_update_utc']
valor_real = float(input('Digite o valor em R$ a ser convertido: '))
cotacao = dados['rates']['BRL']
print(f'O valor R$ {valor_real:.2f} em USD dolar é US${(valor_real / cotacao):.2f}\n'
      f'Atualizado em: {diacotacao}')
