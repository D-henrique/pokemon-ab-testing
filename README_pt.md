# 🎮 Pokémon Battle Strategy — A/B Testing com Python
<p align="center">
  <a href="https://github.com/D-henrique/pokemon-ab-testing/blob/main/README.md">
    <img src="https://img.shields.io/badge/Lang-EN-blue" alt="English" />
  </a>
  <a href="https://github.com/D-henrique/pokemon-ab-testing/blob/main/README_pt.md">
    <img src="https://img.shields.io/badge/Lang-PT--BR-brightgreen" alt="Português" />
  </a>
</p>


> *"Qual estratégia de batalha converte mais treinadores em Campeões?"*  
> Um experimento estatístico aplicado ao universo Pokémon.

---

## 📌 Sobre o Projeto

Este projeto aplica **A/B Testing** a dados reais de Pokémon coletados via [PokéAPI](https://pokeapi.co/), simulando um experimento controlado para comparar duas estratégias de batalha:

- **Grupo A — Estratégia Física:** Pokémon do tipo Fogo priorizando `attack` e `speed`
- **Grupo B — Estratégia Especial:** Pokémon do tipo Água priorizando `special_attack` e `hp`

O objetivo é determinar, com rigor estatístico, qual estratégia apresenta maior taxa de vitória — e se essa diferença é estatisticamente significativa.

---

## 🧪 Hipóteses

| Hipótese | Descrição |
|---|---|
| **H₀ (nula)** | Não há diferença significativa na taxa de vitória entre as estratégias A e B |
| **H₁ (alternativa)** | Uma das estratégias apresenta taxa de vitória significativamente maior |

Critério de decisão: **p-value < 0,05** (nível de significância α = 5%)

---

## 🗂️ Estrutura do Projeto

```
pokemon-ab-testing/
├── data/
│   ├── pokemon_stats.csv        # Dados coletados da PokéAPI
│   └── simulated_battles.csv    # Dados com resultados simulados
├── notebooks/
│   └── analysis.ipynb           # Análise exploratória e visualizações
├── src/
│   ├── fetch_data.py            # Coleta de dados via PokéAPI
│   ├── simulate.py              # Simulação das batalhas
│   └── stats.py                 # Teste estatístico e visualizações
├── outputs/
│   └── ab_test_result.png       # Gráfico com resultado do teste
├── requirements.txt
└── README.md
```

---

## ⚙️ Metodologia

### 1. Coleta de Dados
Dados reais de atributos (`attack`, `special_attack`, `speed`, `hp`) coletados para 40 Pokémon de cada tipo via PokéAPI.

### 2. Simulação do Experimento
Cada Pokémon recebe um `power_score` calculado de acordo com sua estratégia:

```
Grupo A: power_score = attack × 0.6 + speed × 0.4
Grupo B: power_score = special_attack × 0.6 + hp × 0.4
```

A vitória é simulada com `numpy.random.binomial`, usando o `power_score` normalizado como probabilidade — garantindo **reprodutibilidade** com `seed=42`.

### 3. Teste Estatístico
Aplicação do **t-test de Welch** (`scipy.stats.ttest_ind`) para comparar as taxas de conversão (vitória) entre os grupos.

---

## 📊 Resultado

![Resultado do A/B Test](outputs/ab_test_result.png)

| Métrica | Grupo A (Físico) | Grupo B (Especial) |
|---|---|---|
| Taxa de Vitória | — | — |
| T-statistic | — | — |
| p-value | — | — |

> Os valores são gerados na execução. Execute o projeto localmente para ver os resultados completos.

---

## 🚀 Como Executar

**Pré-requisitos:** Python 3.9+

```bash
# Clone o repositório
git clone https://github.com/d-henrique/pokemon-ab-testing.git
cd pokemon-ab-testing

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Execute na ordem
python src/fetch_data.py    # 1. Coleta dados reais da PokéAPI
python src/simulate.py      # 2. Simula as batalhas
python src/stats.py         # 3. Roda o teste e gera o gráfico
```

---

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square)
![Seaborn](https://img.shields.io/badge/Seaborn-4C9BE8?style=flat-square)

| Biblioteca | Uso |
|---|---|
| `pandas` | Manipulação e estruturação dos dados |
| `numpy` | Simulação probabilística com seed controlada |
| `scipy.stats` | Teste t de Welch (ttest_ind) |
| `matplotlib` / `seaborn` | Visualização dos resultados |
| `requests` | Consumo da PokéAPI |

---

## 📚 Conceitos Aplicados

- Desenho experimental (definição de grupos controle e variação)
- Simulação de Monte Carlo com seed reproduzível
- Inferência estatística (t-test, p-value, nível de significância)
- Consumo de API REST e tratamento de dados aninhados (JSON)
- Visualização de resultados experimentais

---

## 👤 Autor

**Douglas Moreira**  
Analista de Dados | Mestrando em Ciência Política (PPGCP/UFPA)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/douglas-moreira-503164bb/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/d-henrique)
