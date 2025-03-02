import requests

URL= 'https://api.pokemonbattle.ru/v2'
TOKEN= '1931ac4fa59c344211bfe37adb35b945'
HEADER= {'Content-type': 'application/json', 'trainer_token': TOKEN}
body_pokemons = {
    "name": "Рафаэль",
    "photo_id": 108 
}
body_change = {
    "pokemon_id": "248810",
    "name": "Рафа",
    "photo_id": 15
}
body_pokeball= {
    "pokemon_id": "248810"
}

'''response = requests.post(url= f'{URL}/pokemons', headers= HEADER, json = body_pokemons )
print(response.text)'''

'''response_change = requests.put(url= f'{URL}/pokemons', headers= HEADER, json = body_change )
print(response_change.text)'''

response_pokeball = requests.post(url= f'{URL}/trainers/add_pokeball', headers= HEADER, json = body_pokeball )
print(response_pokeball.text)
