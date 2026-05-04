import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def run_ab_test():
    df = pd.read_csv("data/simulated_battles.csv")

    group_a = df[df["group"] == "A"]["converted"]
    group_b = df[df["group"] == "B"]["converted"]

    rate_a = group_a.mean()
    rate_b = group_b.mean()

    t_stat, p_value = stats.ttest_ind(group_a, group_b)

    print(f"Taxa de vitória — Grupo A (Físico/Fogo): {rate_a:.2%}")
    print(f"Taxa de vitória — Grupo B (Especial/Água): {rate_b:.2%}")
    print(f"T-statistic: {t_stat:.4f} | p-value: {p_value:.4f}")

    if p_value < 0.05:
        winner = "A" if rate_a > rate_b else "B"
        print(f"\n✅ Diferença significativa! Grupo {winner} vence.")
    else:
        print("\n⚠️ Sem evidência estatística suficiente.")

    # Visualização
    sns.barplot(data=df, x="group", y="converted",
                palette={"A": "#FF6B6B", "B": "#4DABF7"})
    plt.title("Taxa de Vitória por Estratégia de Batalha")
    plt.ylabel("Taxa de Conversão (vitória)")
    plt.xlabel("Grupo (A = Físico | B = Especial)")
    plt.savefig("outputs/ab_test_result.png", dpi=150, bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    run_ab_test()