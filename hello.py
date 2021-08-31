import pandas as pd
import requests

print("oi")

cep_input = input('digite o cep')
print(cep_input)
print()

request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))
print(request.json())