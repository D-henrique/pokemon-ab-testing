import pandas as pd
import numpy as np

def simulate_battles(df, seed=42):
    np.random.seed(seed)
    df = df.copy()

    # Grupo A: estratégia física (usa attack + speed)
    # Grupo B: estratégia especial (usa special_attack + hp)
    df["group"] = np.where(df["type"] == "fire", "A", "B")

    df["power_score"] = np.where(
        df["group"] == "A",
        df["attack"] * 0.6 + df["speed"] * 0.4,
        df["special_attack"] * 0.6 + df["hp"] * 0.4
    )

    # Simula vitória com probabilidade baseada no power_score
    df["win_prob"] = df["power_score"] / df["power_score"].max()
    df["converted"] = np.random.binomial(1, df["win_prob"])

    return df

if __name__ == "__main__":
    df = pd.read_csv("data/pokemon_stats.csv")
    result = simulate_battles(df)
    result.to_csv("data/simulated_battles.csv", index=False)
    print(result.groupby("group")["converted"].mean())