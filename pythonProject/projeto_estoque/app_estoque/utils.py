import requests

def get_address_info(cep):
    url = f'https://viacep.com.br/ws/05863190/json/'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None