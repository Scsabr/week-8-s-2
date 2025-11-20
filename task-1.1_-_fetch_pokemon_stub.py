"""
Exercise 1.1: Fetch and Display a Pokémon (Stub)
- Fetch Pokémon data from the PokéAPI.
- Pretty-print the raw JSON response.
"""

import httpx
import json


def fetch_pokemon(name):
    """Fetch Pokémon data from the PokéAPI and display raw JSON."""
    # TODO: Construct the URL using the Pokémon name (hint: f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")
    response = httpx.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")

    if response.status_code == 200:
        data = response.json()
        for i in data["sprites"]:
            print(i[])

        #print(json.dumps(data, indent=4))
    else:
        print(f"Error: Request failed with status code {response.status_code}")


# Example usage
fetch_pokemon("squirtle")

fetch_pokemon("mew")

"""
Hints:
- Use httpx.get(url) to fetch the data.
- Use response.json() to parse the JSON.
- Use json.dumps(data, indent=4) to pretty-print the JSON.
"""
