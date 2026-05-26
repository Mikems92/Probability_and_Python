# CATALOGUE DE FILMS NETFLIX
catalogue = [
    {"id": 1,  "titre": "ApexAction",        "genre": "Thriller", "duree_min": 96},
    {"id": 2,  "titre": "Red Notice",        "genre": "Action",   "duree_min": 118},
    {"id": 3,  "titre": "The Gray Man",      "genre": "Action",   "duree_min": 122},
    {"id": 4,  "titre": "KPop Demon Hunters","genre": "Animation","duree_min": 100},
    {"id": 5,  "titre": "Ravage",            "genre": "Action",   "duree_min": 107},
    {"id": 6,  "titre": "Triple Frontier",   "genre": "Action",   "duree_min": 125},
    {"id": 7,  "titre": "Land of Bad",       "genre": "Action",   "duree_min": 113},
    {"id": 8,  "titre": "The Mother",        "genre": "Action",   "duree_min": 115},
    {"id": 9,  "titre": "The Old Guard",     "genre": "Action",   "duree_min": 119}, 
    {"id": 10, "titre": "Purple Hearts",     "genre": "Romance",  "duree_min": 122}, 
    {"id": 11, "titre": "Enola Holmes",      "genre": "Adventure", "duree_min": 123},
    {"id": 12, "titre": "Don't Look Up",     "genre": "Comedy",   "duree_min": 143},
    {"id": 13, "titre": "The Irishman",      "genre": "Drama",    "duree_min": 209},
    {"id": 14, "titre": "Glass Onion: A Knives Out Mystery",         "genre": "Comedy",   "duree_min": 139},
    {"id": 15, "titre": "Extraction 2",      "genre": "Action",   "duree_min": 118},
    {"id": 16, "titre": "The Damsel",        "genre": "Fantasy",  "duree_min": 110},
    {"id": 17, "titre": "Bird Box",          "genre": "Thriller",  "duree_min": 124},
    {"id": 18, "titre": "Hustle",            "genre": "Comedy",    "duree_min": 117},
    {"id": 19, "titre": "The Adam Project",       "genre": "Sci-Fi", "duree_min": 106},
    {"id": 20, "titre": "Troll",             "genre": "Action",   "duree_min": 104},
]

 
# ESPACE D'ÉCHANTILLONNAGE
omega = catalogue
N = len(omega)
 
# ÉVÉNEMENTS
A          = [f for f in omega if f["genre"] == "Action"]
B          = [f for f in omega if f["duree_min"] < 120]
 
ids_A      = {f["id"] for f in A}
ids_B      = {f["id"] for f in B}
A_inter_B  = [f for f in omega if f["id"] in ids_A & ids_B]
ids_union  = ids_A | ids_B
A_union_B  = [f for f in omega if f["id"] in ids_union]
complement = [f for f in omega if f["id"] not in ids_union]
 
# PROBABILITÉS
P_A            = len(A) / N
P_B            = len(B) / N
P_inter        = len(A_inter_B) / N
P_union_axiome = P_A + P_B - P_inter
P_union_direct = len(A_union_B) / N
P_complement   = 1 - P_union_axiome
 
# AFFICHAGE CONSOLE
sep = "=" * 57
print(f"\n{sep}")
print("  RÉSULTATS ")
print(sep)
print(f"\n  Espace d'échantillonnage  |Omega| = {N} films\n")
print(f"Événement A  (Action)            : {len(A):>2} films,  P(A)   = {P_A:.2f}")
print(f"Événement B  (< 2h)              : {len(B):>2} films,  P(B)   = {P_B:.2f}")
print(f"Intersection A & B                 : {len(A_inter_B):>2} films, P(A_inter_B) = {P_inter:.2f}")
print(f"\n")
print(f"  Axiome d'additivité :")
print(f"  P(A_union_B) = P(A) + P(B) - P(A_inter_B)")
print(f"         = {P_A:.2f} + {P_B:.2f} - {P_inter:.2f}")
print(f"         = {P_union_axiome:.2f},    (vérif. directe : {P_union_direct:.2f})")
print(f"{'-'*57}")
print(f"\nP(A_union_B)   — Action OU court       :  {P_union_axiome:.2f}  ({P_union_axiome*100:.0f}%)")
print(f"P(Abar_inter_Bbar)  — ni Action ni court     :  {P_complement:.2f}  ({P_complement*100:.0f}%)")
 
print(f"\n{sep}")
print("  INSIGHT BUSINESS")
print(sep)
print(f"\n  {(P_inter)*100:.0f}% du catalogue satisfait au moins un critère.")
print(f"  Seulement {len(complement)} film(s) échappent aux deux filtres :")
for f in complement:
    h, m = divmod(f["duree_min"], 60)
    print(f"[{f['genre']}] {f['titre']} ({h}h{m:02d})")
 
print(f"\n{sep}")
print("  CODE COULEUR DES ÉVÉNEMENTS")
print(sep)
rows = [
    ("Omega",   "Univers complet",  N,         1.00, "Gris"),
    ("A",       "Action",           len(A),    P_A,  "Bleu"),
    ("B",       "Moins de 2h",      len(B),    P_B,  "Vert"),
    ("A_inter_B", "Intersection",   len(A_inter_B), P_inter, "Ambre"),
    ("A_union_B", "Union",          len(A_union_B), P_union_axiome, "Violet"),
    ("Abar_inter_Bbar", "Complémentaire",   len(complement), P_complement, "Rouge"),
]
print(f"\n  {'Évén.':<6} {'Définition':<18} {'Films':>5}  {'P':>5}  Couleur")
print(f"  {'-'*6} {'-'*18} {'-'*5}  {'-'*5}  {'-'*7}")
for sym, defn, n_ev, p, col in rows:
    print(f"{sym:<6} {defn:<18} {n_ev:>5}  {p:>5.2f}  {col}")
