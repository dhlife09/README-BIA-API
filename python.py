import requests

url = 'https://gupsik.biago.ga/api.php'
response = requests.get(url)



if(response.status_code == 200):
    data = response.json()
    print(data['gupsik'])
else:
    print("Error Code:" + response.status_code)
