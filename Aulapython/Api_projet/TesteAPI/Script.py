import requests

#res = requests.get('https://scotch.iO')
res = requests.get('http://192.168.179.6:8000/')

#print(res)

print(res.headers)

if res:
    print('Response OK')
else:
    print('Response Failed')




    #print(res.status_code)