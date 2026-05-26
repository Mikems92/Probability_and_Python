# Netflix Movies Probability Engine

## Objectif du projet

Un utilisateur ouvre Netflix et clique au hasard sur un film.  
**Quelle est la probabilité qu'il tombe sur un film Action OU de moins de 2h ?**

Ce mini-projet traduit une question business concrète en modèle probabiliste formel,  
en appliquant strictement les **axiomes de Kolmogorov** (Chapter 1 du MITx 6.431x — Probability — The Science of Uncertainty and Data).


## Code couleur des événements

| Couleur | Événement | Définition | Films | P |
|---------|-----------|-----------|:-----:|:---:|
| ⬜ Gris   | **Ω**    | Univers complet          | 20 | 1.00 |
| 🔵 Bleu   | **A**    | Films d'Action           |  9 | 0.45 |
| 🟢 Vert   | **B**    | Films < 2h (< 120 min)   | 12 | 0.60 |
| 🟡 Ambre  | **A∩B**  | Action ET < 2h           |  7 | 0.35 |
| 🟣 Violet | **A∪B**  | Action OU < 2h           | 14 | 0.70 |
| 🔴 Rouge  | **Ā∩B̄**  | Ni Action ni court       |  6 | 0.30 |

---

## Fondations mathématiques

### 1. Espace d'échantillonnage (Sample Space)

$$\Omega = \{f_1, f_2, \ldots, f_{20}\}, \quad |\Omega| = 20$$

Modèle **discret uniforme** : chaque film a une probabilité égale $\frac{1}{20} = 0{,}05$.

### 2. Événements (Set Theory)

$$A = \{f \in \Omega \mid \text{genre}(f) = \text{Action}\}, \quad |A| = 9$$

$$B = \{f \in \Omega \mid \text{durée}(f) < 120 \text{ min}\}, \quad |B| = 12$$

$$A \cap B = \{f \mid f \in A \text{ et } f \in B\}, \quad |A \cap B| = 7$$

### 3. Axiome d'additivité

$$\boxed{P(A \cup B) = P(A) + P(B) - P(A \cap B) = \frac{9}{20} + \frac{12}{20} - \frac{7}{20} = \frac{14}{20} = 0{,}70}$$

> ⚠️ **Le piège du double comptage** : sans soustraire $P(A \cap B)$, les 7 films  
> "Action ET courts" seraient comptés deux fois → résultat faux de $\frac{21}{20} > 1$ (impossible !).

### 4. Loi du complémentaire (3e axiome)

$$P(\bar{A} \cap \bar{B}) = 1 - P(A \cup B) = 1 - 0{,}70 = 0{,}30$$

---

## Catalogue complet (Ω — 20 films)

| # | Titre | Genre | Durée | A | B |
|:-:|-------|-------|:-----:|:-:|:-:|
| 1  | ApexAction                          | Thriller  | 1h36 |   | ✓ |
| 2  | Red Notice                          | Action    | 1h58 | ✓ | ✓ |
| 3  | The Gray Man                        | Action    | 2h02 | ✓ |   |
| 4  | KPop Demon Hunters                  | Animation | 1h40 |   | ✓ |
| 5  | Ravage                              | Action    | 1h47 | ✓ | ✓ |
| 6  | Triple Frontier                     | Action    | 2h05 | ✓ |   |
| 7  | Land of Bad                         | Action    | 1h53 | ✓ | ✓ |
| 8  | The Mother                          | Action    | 1h55 | ✓ | ✓ |
| 9  | The Old Guard                       | Action    | 1h59 | ✓ | ✓ |
| 10 | Purple Hearts                       | Romance   | 2h02 |   |   |
| 11 | Enola Holmes                        | Adventure | 2h03 |   |   |
| 12 | Don't Look Up                       | Comedy    | 2h23 |   |   |
| 13 | The Irishman                        | Drama     | 3h29 |   |   |
| 14 | Glass Onion: A Knives Out Mystery   | Comedy    | 2h19 |   |   |
| 15 | Extraction 2                        | Action    | 1h58 | ✓ | ✓ |
| 16 | The Damsel                          | Fantasy   | 1h50 |   | ✓ |
| 17 | Bird Box                            | Thriller  | 2h04 |   |   |
| 18 | Hustle                              | Comedy    | 1h57 |   | ✓ |
| 19 | The Adam Project                    | Sci-Fi    | 1h46 |   | ✓ |
| 20 | Troll                               | Action    | 1h44 | ✓ | ✓ |

**Zones du diagramme de Venn :**

- **A seulement** *(Action, ≥ 120 min)* : The Gray Man, Triple Frontier — 2 films
- **A ∩ B** *(Action ET < 120 min)* : Red Notice, Ravage, Land of Bad, The Mother, The Old Guard, Extraction 2, Troll — 7 films
- **B seulement** *(non-Action, < 120 min)* : ApexAction, KPop Demon Hunters, The Damsel, Hustle, The Adam Project — 5 films
- **Ā∩B̄** *(ni Action ni court)* : Purple Hearts, Enola Holmes, Don't Look Up, The Irishman, Glass Onion, Bird Box — 6 films

<img width="1075" height="1174" alt="venn_streamviz" src="https://github.com/user-attachments/assets/5e2bf53c-8d2e-49c9-8871-2f7853afebfd" />


## 🛠️ Stack technique

- **Python 3** — pur, sans librairies externes pour la logique probabiliste


## ▶️ Utilisation

```bash
# Résultats console uniquement
python netflix_movies.py

## Concepts MITx illustrés

| Concept | Implémentation Python |
|---------|----------------------|
| Sample Space $\Omega$ | `catalogue` (liste de 20 dicts) |
| Événement = sous-ensemble | List comprehension `[f for f in omega if ...]` |
| Union $A \cup B$ | `ids_A \| ids_B` |
| Intersection $A \cap B$ | `ids_A & ids_B` |
| Axiome d'additivité | `P_A + P_B - P_inter` |
| Complémentaire | `1 - P_union` |
| Vérification | Double calcul direct vs axiome |

---

## Référence académique

> *"6.431x — Probability — The Science of Uncertainty and Data"*  
> MITx MicroMasters in Statistics and Data Science  
> Unit 1 : Probability Models and Axioms

---

*Projet réalisé dans le cadre de l'apprentissage des fondations probabilistes — niveau débutant, logique rigoureuse.*
