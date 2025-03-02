import requests
import pytest 

URL= 'https://api.pokemonbattle.ru/v2'
TOKEN= '1931ac4fa59c344211bfe37adb35b945'
HEADER= {'Content-type': 'application/json', 'trainer_token': TOKEN}
trainer_id = 22638

def  test_status_code ():
    response = requests.get(url= f'{URL}/trainers', params = {'trainer_id': trainer_id})
    assert response.status_code == 200
