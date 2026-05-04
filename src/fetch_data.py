import requests
import pandas as pd

def get_pokemon_by_type(type_name):
    url = f"https://pokeapi.co/api/v2/type/{type_name}"
    r = requests.get(url).json()
    pokemons = []

    for entry in r["pokemon"][:40]:  # limite para não sobrecarregar
        name = entry["pokemon"]["name"]
        poke = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}").json()
        stats = {s["stat"]["name"]: s["base_stat"] for s in poke["stats"]}
        pokemons.append({
            "name": name,
            "type": type_name,
            "attack": stats.get("attack", 0),
            "special_attack": stats.get("special-attack", 0),
            "speed": stats.get("speed", 0),
            "hp": stats.get("hp", 0),
        })

    return pd.DataFrame(pokemons)

if __name__ == "__main__":
    fire = get_pokemon_by_type("fire")
    water = get_pokemon_by_type("water")
    df = pd.concat([fire, water])
    df.to_csv("data/pokemon_stats.csv", index=False)
    print("Dados salvos!")