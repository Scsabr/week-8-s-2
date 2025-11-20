"""
Exercise 2.3: Remove Pokémon from the Team (Stub)
- Implement a method to remove a Pokémon from the team by name.
- Make sure the team size is updated accordingly.
"""

import httpx

class Team:
    def __init__(self):
        """Initialise an empty team."""
        self.members = []
    
    def add_pokemon(self, name):
        response = httpx.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")
        if response.status_code == 200:
            data = response.json()

            name = data["name"]

            types = [ t["type"]["name"] for t in data["types"] ]

            stats = {}
            for i in data["stats"]:
                stats[i["stat"]["name"]] = i["base_stat"]

            image_url = data["sprites"]["front_default"]

            pokemon = {}
            pokemon["name"] = name
            pokemon["types"] = types
            pokemon["stats"] = stats
            pokemon["image"] = image_url

            self.members.append(pokemon)

        else:
            print(f"Error: Pokémon '{name}' not found!")
    
    def view_team(self):
        """View the current team with details."""
        # (Implementation from Exercise 2.2)
        for ind, i in enumerate(self.members):
            print(f"{ind+1} - {i["name"]}")
            print(f"  Types: {",".join(i["types"])}")
            print("  Base Stats:")
            for stat, value in i["stats"].items():
                print(f"   {stat.capitalize()}: {value}")
            print(f"  Image URL: {i["image"]}")
        print("\n\n")
    
    def remove_pokemon(self, name):
        """Remove a Pokémon from the team by name."""
        # TODO: Find the Pokémon in the team
            # TODO: If found, remove it and print a confirmation message
            # TODO: If not found, print a message indicating the Pokémon is not in the team
        if self._is_in_team(name):
            for ind, i in enumerate(self.members):
                if i["name"] == name:
                    self.members.pop(ind)
                    return True
        else:
            print(f"Could not find {name} in your team :(")


    def _is_in_team(self, name):
        for i in self.members:
            if i["name"] == name:
                return True
        return False

    


# Example usage
team = Team()
team.add_pokemon("squirtle")
team.add_pokemon("charmander")
team.view_team()
team.remove_pokemon("squirtle")
team.view_team()
