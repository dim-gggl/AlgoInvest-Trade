# <div align='center'> 🇬🇧 ALGORITHMS </br><em>(Knapsack)</em>

## <div align='center'> ✨ AlgoInvest&Trade ✨
*Invest with algorithms*

This program was created for a school project with the goal of implementing two types of algorithms to solve the classic knapsack problem.

For the fictional company **AlgoInvest&Trade**, the task is to build the **most profitable asset portfolio** possible while respecting a **maximum budget of €500**.

### <div align='center'> Two methods:

- **Brute force**: exhaustively explores every possible combination.
- **Dynamic programming**: optimized strategy designed for large datasets.

---

## <div align='center'> 🧰 Installation

### 1. Clone or download this repo
```bash
git clone https://github.com/dim-gggl/AlgoInvest-Trade.git
cd AlgoInvest-Trade
```
(Or click the green “Code” button at the top of this page ➚ > “Download ZIP” > extract on your desktop)

### 2. **Set up a virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate    # macOS / Linux
.venv\Scripts\activate       # Windows
```
>Note: This program doesn’t require any third-party modules and relies only on the Python standard library.

## <div align='center'> Run the program

### Apply an algorithm to a dataset

#### Option 1:
- Directly via `main.py`


```bash
python3 main.py
```


#### Option 2:
- You can pass options to the command in your terminal:

```bash
# Run dynamic programming algorithm
python3 main.py -dp

# Specify a different CSV file
python3 main.py -f <path/to/file>
# (default: data/Liste_actions.csv)

# Combine both options
python3 main.py -dp -f <path/to/file>
```

The program will ask directly afterward if you want to display the differences between algorithm choice and Sienna's choice (Financial advisor of AlgoInvest&Trade)

### <div align='center'>Display report for invalid data

There's a lot of unusable data in the datasets. To display a report showing the details about those:

```bash
python3 report.py
```

And then just follow the prompt.

---
## <div align='center'> 📊 Algorithms: </br><em>advantages, limits & complexity</em>

</br>

### <div align='center'> `bruteforce.py` O(2^n)

#### Pseudo-code
```plaintext
Function brute_force(actions, budget)
    best_cost   ← 0
    best_combo  ← []
    best_profit ← 0
    n ← number of actions

    For i from 1 to n do
        For each combo of size i in itertools.combinations(actions, i) do
            total_cost ← sum(cost of each action in combo)
            If total_cost <= budget then
                total_profit ← sum(profit of each action in combo)
                If total_profit > best_profit then
                    best_profit ← total_profit
                    best_cost   ← total_cost
                    best_combo  ← combo
                End If
            End If
        End For
    End For

    Return (best_cost, best_combo, best_profit)
End Function
```

### **Principle** :
- Tests every possible combination, from a single asset up to all assets together. For each combination, checks that the total cost doesn’t exceed the budget. After evaluating all combinations, returns the optimal solution — i.e., the most profitable one.
### **Advantage** :
- Guarantees the absolute best result, since all possibilities are explored.
### **Limit** :
- Extremely slow as the number of assets grows (time complexity ≃ O(2ⁿ)).
### **Use case** :
- Ideal for small sets (fewer than ~20–22 assets).
</br>
</br>

---

### <div align='center'> `optimized.py` O(n*W)

#### Pseudo-code
```plaintext
Function optimized(actions, budget)
    n ← number of actions
    B ← budget * 100  // convert to cents

    dp   ← array of size (B + 1) initialized to 0
    keep ← matrix (n × (B + 1)) initialized to FALSE
    min_cost ← minimum(action.cost * 100 for action in actions)

    For i from 0 to n-1 do
        cost   ← actions[i].cost * 100
        profit ← actions[i].profit
        For b from B down to cost do
            If dp[b - cost] + profit > dp[b] then
                dp[b] ← dp[b - cost] + profit
                keep[i][b] ← TRUE
            End If
        End For
    End For

    b ← B
    selected_actions ← []
    For i from n-1 down to 0 do
        If keep[i][b] then
            Append actions[i] to selected_actions
            b ← b - (actions[i].cost * 100)
        End If
    End For

    total_cost   ← sum(action.cost for action in selected_actions)
    total_profit ← sum(action.profit for action in selected_actions)

    Return (total_cost, selected_actions, total_profit)
End Function
```

### **Principle** :
- dynamic programming algorithm inspired by the classic knapsack problem. Instead of repeating the same calculations multiple times like brute force, it stores intermediate results in memory and, as it progresses, compares new results with stored ones to choose the optimal solution.
### **Advantage** :
- very fast even on large datasets (time complexity ≃ O(n × W), where W = budget).
### **Limit** :
- can be less readable for those unfamiliar with dynamic programming.
### **Use Case** :
- recommended for more than ~20 assets.

</br>
</br>

---

## <div align='center'> ✨ Contact

Project completed as part of the “Python Web Application Development” path at OpenClassrooms.

- **GitHub**: [@dim-gggl](https://github.com/dim-gggl)
- **Email** : dimitri.gaggioli@gmail.com

---
</br>
<br>
</br>


# <div align='center'>🇫🇷 ALGORITHMES 🇫🇷<br>_(Sac à dos)_

## <div align='center'>✨ AlgoInvest&Trade✨ <br>_investir avec algorithme_
</br>
Ce programme répond à un projet d'études ayant pour consigne d'inviter à implémenter deux types d'algorithmes pour répondre au célèbre problème du sac à dos (ou "knapsack problem").

Ici, pour la société fictive AlgoInvest&Trade, il s'agit de concevoir le **meilleur portefeuille d'actifs possible** tout en respectant un budget maximum de 500 euros.

Deux méthodes :

- une stratégie exhaustive (force brute) qui cherche *toutes* les combinaisons possibles,
- une stratégie optimisée (programmation dynamique) pensée pour les gros volumes.

---

## <div align='center'>🧰 **Installation** 🧰

### 1. Cloner ou télécharger ce repo

```
git clone https://github.com/dim-gggl/AlgoInvest-Trade.git
cd AlgoInvest-Trade
```
Sinon, cliquez sur le bouton vert "Code" (en haut de cette page ➚) > "Download ZIP" > extraire sur votre bureau

### 2. **Installer un environnement virtuel**

```
python3 -m venv .venv
source .venv/bin/activate   # sur macOS ou Linux
venv\Scripts\activate       # sur Windows
```
>Note : Ce programme ne nécessite pas l'emploi de modules tiers et ne se base que sur la bibliothèque Python standard.

## <div align='center'> 🚀 Lancer le programme

### Appliquer un algorithme sur une base de donnée
### Option 1 :
- Directement dans `main.py`

```bash
python3 main.py
```
Et se laisser guider.


### Option 2:
- en ligne de commande :

```bash
# Algo de programmation dynamique
python3 main.py -dp

# Spécifier un autre fichier CSV
python3 main.py -f <chemin/vers/fichier>
# (défaut : data/Liste_actions.csv)

# Combinaison des deux
python3 main.py -dp -f <chemin/vers/fichier>
```
### Afficher un rapport sur les données corrompues

Les bases de données fournies comportent un certain nombre de données invalides.
Pour en afficher un rapport détaillé:

```bash
python3 report.py
```
Et se laisser guider par le programme.

---

## <div align='center'> 📊 Algorithmes : <br><em>avantages, limites et complexités</em>
</br>

### <div align='center'> `bruteforce.py` O(2^n)
#### Pseudo-code
```plaintext
Fonction brute_force(actions, budget)
    meilleur_cout   ← 0
    meilleur_combo  ← []
    meilleur_profit ← 0
    n ← nombre d'actions dans actions

    Pour i de 1 à n faire
        Pour chaque combo de taille i dans itertools.combinations(actions, i) faire
            coût_total ← somme des coûts des actions dans combo
            Si coût_total <= budget alors
                profit_total ← somme des profits des actions dans combo
                Si profit_total > meilleur_profit alors
                    meilleur_profit ← profit_total
                    meilleur_cout   ← coût_total
                    meilleur_combo  ← combo
                Fin Si
            Fin Si
        Fin Pour
    Fin Pour

    Retourner (meilleur_cout, meilleur_combo, meilleur_profit)
Fin Fonction
```


### **Principe** :
- Teste toutes les combinaisons possibles, comprenant d'une seule action jusqu'à combiner l'intégralité du lot. Vérifie, pour chaque combinaison, que son coût total n'excède pas le budget, Une fois toutes les opérations effectuées sur chacune des combinaisons possibles, renvoie la solution optimale, à savoir, ici, la plus rentable.
### **Avantage** :
- Garantit le meilleur résultat, avec certitude, puisque tout est tenté.
### **Limite** :
- Très lent dès que le nombre d'actions augmente (complexité ∅ **O(2^n)**)
### **Utilisation** :
- Idéale pour petits ensembles (moins de 20-22 actions)
</br>

</br>

### <div align='center'> `optimized.py` O(n*W)

#### Pseudo-code
```plaintext
Fonction optimized(actions, budget)
    n ← nombre d'actions
    B ← budget * 100  // conversion en centimes

    dp   ← tableau de taille (B + 1) initialisé à 0
    keep ← matrice (n × (B + 1)) initialisée à FAUX
    min_cost ← min(action.cost * 100 pour action dans actions)

    Pour i de 0 à n-1 faire
        cost   ← actions[i].cost * 100
        profit ← actions[i].profit
        Pour b de B à cost (pas -1) faire
            Si dp[b - cost] + profit > dp[b] alors
                dp[b] ← dp[b - cost] + profit
                keep[i][b] ← VRAI
            Fin Si
        Fin Pour
    Fin Pour

    b ← B
    selected_actions ← []
    Pour i de n-1 à 0 (pas -1) faire
        Si keep[i][b] alors
            Ajouter actions[i] à selected_actions
            b ← b - (actions[i].cost * 100)
        Fin Si
    Fin Pour

    total_cost   ← somme des action.cost pour action dans selected_actions
    total_profit ← somme des action.profit pour action dans selected_actions

    Retourner (total_cost, selected_actions, total_profit)
Fin Fonction
```

### **Principe** :
- Algorithme de programmation dynamique inspiré du knapsack. Contrairement à l'approche naïve de force brute qui réitère les mêmes opérations plusieurs fois, la programmation dynamique stocke en mémpoire les résultats des opérations déjà effectuées et compare, à mesure d'avancement, les résultats obtenues avec ceux stockées en mémoire pour choisir la solution optimale.
### **Avantage** :
- très rapide même sur gros volumes (complexité ∅ **O(n × W)** avec W=budget)
### **Limite** :
- peut être moins lisible pour les non-initiés
### **Utilisation** :
- recommandé au-delà de 20 actions
</br>


---

## <div align='center'> ✨ Contact

Projet réalisé dans le cadre du parcours "Developement d'applications Web Python" chez OpenClassrooms.

- **GitHub** : [@dim-gggl](https://github.com/dim-gggl)
- **Mail**   : dimitri.gaggioli@gmail.com
