#!/usr/bin/env python3
"""
Task 1.2: Summarise Pokemon
This script demonstrates how to store and display Pokemon information.
"""

def get_pokemon_data():
    """
    Returns a dictionary containing Pokemon information.
    """
    pokemon = {
        "name": "Pikachu",
        "type": ["Electric"],
        "level": 25,
        "hp": 60,
        "attack": 55,
        "defense": 40,
        "abilities": ["Static", "Lightning Rod"],
        "moves": ["Thunder Shock", "Quick Attack", "Thunder Wave", "Electro Ball"]
    }
    return pokemon


def print_pokemon_summary(pokemon):
    """
    Prints a summary of the Pokemon's details in a readable format.
    
    Args:
        pokemon (dict): A dictionary containing Pokemon information
    """
    print("=" * 50)
    print(f"Pokemon Summary: {pokemon['name']}")
    print("=" * 50)
    print(f"Type: {', '.join(pokemon['type'])}")
    print(f"Level: {pokemon['level']}")
    print(f"\nStats:")
    print(f"  HP: {pokemon['hp']}")
    print(f"  Attack: {pokemon['attack']}")
    print(f"  Defense: {pokemon['defense']}")
    print(f"\nAbilities: {', '.join(pokemon['abilities'])}")
    print(f"\nMoves:")
    for move in pokemon['moves']:
        print(f"  - {move}")
    print("=" * 50)


def main():
    """
    Main function to demonstrate Pokemon summary.
    """
    pokemon_data = get_pokemon_data()
    print_pokemon_summary(pokemon_data)


if __name__ == "__main__":
    main()
