import requests


headers ={
    'Accept': '*/*',
    'User-Agent': 'request'}
url="http://dummy.restapiexample.com/api/v1/employee/1"

resposta = requests.get(url, headers=headers)

resposta_dict =resposta.json()

print(resposta_dict['status'])
print("========================\n")
print(resposta_dict['data'])
