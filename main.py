
import requests
import random

url = "https://pokeapi.co/api/v2/pokemon/"
pokemon_list = ["pikachu", "eevee", "ditto", "snorlax", "mew"]

def get_pokemon(name):
    try:
        response = requests.get(url + name, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError:
        return None
    except requests.exceptions.RequestException:
        return "error"

answer = random.choice(pokemon_list)
pokemon = get_pokemon(answer)

if pokemon == "error":
    print("Connection error!")
elif pokemon is not None:
    print("WHO'S THAT POKEMON?")
    print("Height:", pokemon["height"])
    print("Weight:", pokemon["weight"])

    for i in range(3):
        guess = input("Guess the Pokemon: ").lower().strip()
        result = get_pokemon(guess)

        if result == "error":
            print("Connection error!")
            break
        elif result is None:
            print("Pokemon not found!")
        elif result["name"] == answer:
            print("Correct! You win!")
            break
        else:
            print("Wrong guess!")
    else:
        print("The Pokemon was", answer.title())