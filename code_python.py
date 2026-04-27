#Afficher du texte 
"""print("bonjour")
#Cree des variable et Demander une information a l'utilisateur avec input
nom=input("Quel est ton nom ? ")
age=int(input("Quel est ton age ? "))
taille=float(input("Quel est ta taille ? "))
print(f"Je m'appelle {nom} et j'ai {age + 2} ans")
######################OU###############################
print("tu t'appelle", nom, "tu as",str(age + 2) + "ans","et tu mesure",str(taille + 1) + "m")"""


#Les conditions (if,else)
#Une seule condition
"""age = 17
if age >= 18:
    print("tu es majeur")
else:
    print("tu es mineur")
#Plusieurs conditions
note = 19
if note >= 16:
    print("tres bien")
elif note >= 10:
    print("passable")
else:
    print("echec")
#Avec input
age=int(input("Quel est ton age ? "))
if age >= 18:
    print("acces autoriser")
else:
    print("acces refuser")
#Avec logique (and et ou)
age=20
argent=5000
if age >= 18 and argent >= 2000
    print("acces autoriser")
else:
    print("acces refuser") """


#Les boucles(for, while)
"""for i in range(3): #range(3)= 5 repetition
    print(i)
#pour
for i in range(1, 3): #range(debut, fin, pas)
    print(f"Nombre : {i + 1}")
#pour avec liste
noms = ["Adama", "Ali", "Fatou"]
for nom in noms:  #repetition = egale nombre de noms
    print(f"bonjour {nom}")
#tant que
i = 0
while i < 5:
    print(i)
    i += 1
#Avec continue
for i in range(5):
    if i == 2:  #ignore 2
        continue
    print(i)
#Avec break
for i in range(5):
    if i == 2:  #stop a partir de 2
        break
    print(i) 
#table de multiplication
for i in range(1,11):
    print(f"5 * {i} = {5 * i}")
#demander un nombre et afficher tous les nombre paire jusqu'a ce nombre
n = int(input("Donne un nombre : "))
for i in range(2, n + 1, 2): # n+1 permet d'inclure le nombre si elle est paire
    print(i) 
#l'utilisateur doit deviner un nombre 
nombre_secret = 7
while True:
    proposition = int(input("devine le nombre : "))
    if proposition < nombre_secret:
        print("trop petit")
    elif proposition > nombre_secret:
        print("trop grand")
    else:
        print("bravo !")
        break 
#Avec random le nombre change a chaque fois 
import random 
nombre_secret = random.randint(1, 10)
while True:
    proposition = int(input("devine le nombre : "))
    if proposition < nombre_secret:
        print("trop petit")
    elif proposition > nombre_secret:
        print("trop grand")
    else:
        print("bravo !")
        break """


#cree une liste 
"""nom = ["Adama", "Ali", "Fatou"]
notes = [12,15,9,18]
#Afficher premier element
print(nom[0])
#Afficher dernier element
print(nom[-1])
#Afficher tous
print(nom)
#Modifier un element
nom[1] = "Omar"
#Ajouter des elements a la fin 
nom.append("Awa")
#Ajouter des elements a une position precise
nom.insert(1,"Moussa") 
#Supprime un element
nom.remove("Awa")
del nom[0]
#taille de la liste 
print(len(nom))
#parcourir une liste
for nom in nom:
    print(nom)
for i, nom in enumerate(nom):
    print(f"{i} - {nom}")
#Statistique d'une liste
print(sum(notes))          
print(max(notes))          
print(min(notes))          
print((notes))          
moyenne = sum(notes)/len(notes)
print(moyenne) 
nom = ["Adama", "Ali", "Fatou"]
notes = [12,15,9,18]
#Afficher bonjour nom pour  chaque personne
for nom in nom: 
    print("bonjour", nom)
#Demander 5 nombre a l'utilisateur et les stockés dans une liste
nombre = [] #liste vide
for i in range(5):
    n = int(input("entre un nombre : "))
    nombre.append(n)
    print(nombre)  """


#Dictionnaire
#Cree Dictionnaire
""" personne = { "nom": "Adama", "age": 25, "ville": "Ouagadougou" }
print(personne["nom"])
#Modifier une valeur 
personne["age"] = 26
print(personne["age"])
#Ajouter une nouvelle cle
personne["profession"] = "Data Analyst"
#supprimer une cle
del personne["ville"]
print(personne)
#Parcourir un dictionnaire
for cle in personne: #Affiche les cles
    print(cle)
for valeur in personne.values():  #Affiche les valeurs
    print(valeur)
for cle, valeur in personne.items():  #Affiche les cles et valeurs
    print(f"{cle} : {valeur}") """


#Les fonctions 
"""def dire_bonjour(nom):
    print(f"bonjour {nom}")
dire_bonjour("Adama")
#fonction avec return
def addition(a, b):
    return a+b
print(addition(2, 3))
#fonction avec plusieurs parametre 
def presentation(nom, age):
    age = int(age)
    print(f"{nom} a {age} ans")
presentation("ada", 15)
#fonction avec valeur par defaut
def saluer(nom="ami"):
    print(f"bonjour {nom}")
saluer("ad")  """


#introduction a pandas(pip install pandas)
"""import pandas as pd 
#lire fichier
df = pd.read_csv("pib_bf.csv", sep = ";")
#print(df)
#Afficher une colonne precise
#print(df["PIB nominal en milliards de FCFA"])
#selectionner plusieurs colonnes
#print(df[["colonne","colonne"]])
#Afficher les premieres ligne
print(df.head())
#Afficher les dernieres ligne
print(df.tail())
#Structure des donnée
print(df.info())
#Dimension des donnees
print(df.shape)
#donne types des données 
print(df.dtypes)
#Statistiques
print(df.describe())
df["colonne"].mean()
#donne effectif (frequence)
df["colonne"].value_counts()
#donne proportion (pourcentage)
df["colonne"].value_counts(normalize=True)
#donne les modalité
df["colonne"].unique()
#pour voir la liste des colonnes
df.columns
#trier les donnees
df.sort_values("colonne", ascending=False)
#Filtrer les donnes 
df[df["colonne"]>25]
#Filtrer avec plusieurs conditions(&=et; |=ou)
df[(df["colonne"]>25) & (df["colonne"]=="Bobo")]
#Filtrer + selectionner
df.loc[df["colonne"]>25, ["colonne","colonne"]]
#Filtrer les lignes qui contienne A
df[df["colonne"].str.contains("A")]
#Filtrer par position
df.iloc[0:3, 0:2]
#Ajouter une colonne
df["colonne"] = [1205,2201,2155]
#Ajouter une colonne calculer
df["colonne"] = df["colonne"] + 8
#Modifier les types de données
#Convertir en numérique
df["colonne"] = df["colonne"].astype(int)
#Convertir en texte (caractère)
df["colonne"] = df["colonne"].astype(str)
#Convertir en float 
df["colonne"] = df["colonne"].astype(float)
#Convertir en booléen
df["colonne"] = df["colonne"].astype(bool)
#Convertir en date
df["colonne"] = pd.to_datetime(df["Date"])
#Le type "facteur"
df["colonne"] = df["colonne"].astype("category")
df["colonne"].cat.categories #Vérifier les catégories
# Définir l’ordre
df["colonne"] = df["colonne"].cat.reorder_categories(
    ["Faible", "Moyen", "Élevé"],
    ordered=True
)
Option
errors="raise"
erreur (par défaut)
errors="coerce"
remplace par NaN 
errors="ignore"
ne change rien
#Valeur manquantes
#Voir les valeurs manquantes (True/False)
df.isna()
#Compter les valeurs manquantes par colonne
df.isna().sum()
#Vérifier s’il y a des valeurs manquantes
df.isna().any()
#Supprimer les valeurs manquantes
#Supprimer les lignes contenant des NaN
df.dropna()
#Remplacer les valeurs manquantes
#Remplacer par une valeur fixe
df["Age"] = df["Age"].fillna(0)
#Remplacer par la moyenne
df["Age"] = df["Age"].fillna(df["Age"].mean())
#Remplacer par la valeur la plus fréquente (mode)
df["Ville"] = df["Ville"].fillna(df["Ville"].mode()[0])
#Remplissage vers l’avant (forward fill)
df.fillna(method="ffill")
#Remplissage vers l’arrière (backward fill)
df.fillna(method="bfill")
Type de variable
Méthode recommandée
Numérique
moyenne / médiane
Qualitative
mode
Temporelle
ffill / bfill 
#Doublons 
#Détecter les doublons
#Voir les lignes dupliquées
df.duplicated()
#Voir uniquement les doublons
df[df.duplicated()]
#Compter les doublons
df.duplicated().sum()
#Supprimer les doublons
#Supprimer les lignes dupliquées
df.drop_duplicates()
#Supprimer en gardant le premier doublons 
df.drop_duplicates(keep="first")
#Supprimer en gardant le dernier doublons 
df.drop_duplicates(keep="last")
#Supprimer toutes les doublons 
df.drop_duplicates(keep=False)
#Doublons sur une colonne spécifique
#Supprime les doublons basés sur la colonne Nom
df.drop_duplicates(subset=["Nom"])
#Parfois les doublons ne sont pas exacts :"Ali" ≠ "ali"
#Tout en minuscule 
df["Nom"] = df["Nom"].str.lower().str.strip()
#Première lettre en majuscule 
df["Nom"] = df["Nom"].str.lower().str.strip().str.capitalize()
#Fusion
#Fusion horizontale
df = pd.merge(df1, df2, on="ID")
df = pd.concat([df1, df2], axis=1)
#Fusion verticale
df = pd.concat([df1, df2])
df = pd.concat([df1, df2], axis=0)
#axis=0 → vertical (↓)
#axis=1 → horizontal (→)
#Les types de jointures
#INNER JOIN (intersection)
pd.merge(df1, df2, on="ID", how="inner")
#LEFT JOIN (gauche)
pd.merge(df1, df2, on="ID", how="left")
#RIGHT JOIN (droite)
pd.merge(df1, df2, on="ID", how="right")
#OUTER JOIN (total)
pd.merge(df1, df2, on="ID", how="outer")
#le recodage
#Avec replace()
df["Sexe"] = df["Sexe"].replace({
    "Homme": 1,
    "Femme": 0
})
#Avec map()
df["Sexe"] = df["Sexe"].map({
    "Homme": 1,
    "Femme": 0
})
Différence importante
replace()
garde valeurs inconnues
map()
met NaN si non défini
#Recodage avec condition
df["Statut"] = np.where(df["Age"] >= 18, "Adulte", "Mineur")
#Recodage avec plusieurs conditions (apply)
df["Niveau"] = df["Age"].apply(
    lambda x: "Jeune" if x < 25 else "Adulte"
)
#Recodage en classes
df["Classe_age"] = pd.cut(
    df["Age"],
    bins=[0, 18, 30, 60],
    labels=["Enfant", "Jeune", "Adulte"]
)
df["Classe_revenu"] = pd.qcut(
    df["Salaire"],
    q=4,
    labels=["Bas", "Moyen", "Haut", "Très haut"]
) """


#Graphique 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
df = pd.read_csv("pib_bf.csv", sep = ";")
# ==========================================
#Courbe d'evolution
# ==========================================
# x = points horizontaux, y = points verticaux
"""x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 5, 4, 8, 7, 9, 12, 11, 15, 14, 18]
# 2. CRÉATION DU STYLE
# On crée la figure (l'image) et l'axe (le graphique)
fig, ax = plt.subplots(figsize=(10, 6))
#Change la couleur de toute l'image
#fig.patch.set_facecolor("#121212")
#Change la couleur du graphe
#ax.set_facecolor("#121212")
# On trace la courbe principale (Bleu foncé, trait épais)
ax.plot(x, y, color='#1A5276', linewidth=5, label='Ma donnée')
# L'effet "Stylé" : On remplit l'espace sous la courbe avec un bleu clair transparent
ax.fill_between(x, y, color='#AED6F1', alpha=0.4)
# 3. NETTOYAGE DU GRAPHIQUE 
# On enlève les bordures du haut et de droite pour faire moins "scolaire"
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# On change la couleur des axes restants en gris clair
ax.spines['left'].set_color('#BDC3C7')
ax.spines['bottom'].set_color('#BDC3C7')
# On ajoute une grille uniquement horizontale pour la lecture
ax.grid(True, linestyle='--', alpha=0.5, axis='y')
# 4. TITRES ET TEXTES
ax.set_title('TITRE DU GRAPHIQUE', loc='left', fontsize=18, fontweight='bold', color='#2C3E50', pad=20)
ax.set_xlabel('Légende Axe X', color='#7F8C8D')
ax.set_ylabel('Légende Axe Y', color='#7F8C8D')
# On ajuste les marges pour que rien ne soit coupé
plt.tight_layout()
# On affiche le résultat
plt.show() """
# ==========================================
#Histogramme
# ==========================================
#DONNÉES
# On simule 1000 notes d'examen ou mesures (moyenne de 12, écart de 3)
"""donnees = np.random.normal(12, 3, 1000) 
#CRÉATION DU CADRE ET DU DESSIN 
# Fond gris très clair (#F8F9FA)
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#F8F9FA')
ax.set_facecolor('#F8F9FA')
#TRACÉ DE L'HISTOGRAMME
n, bins, patches = ax.hist(donnees, 
                           bins=20, # Nombre de "barres"
                           color='#1A5276', # Bleu foncé
                           edgecolor='#F8F9FA', # Bordure des barres (pour les séparer proprement)
                           linewidth=1.2, #Epaisseur de la ligne qui entoure chaque barre
                           alpha=0.85) # Légère transparence pour le style
#NETTOYAGE ET STYLE 
# On enlève les bordures inutiles
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# Couleur discrète pour les axes restants
ax.spines['left'].set_color('#BDC3C7')
ax.spines['bottom'].set_color('#BDC3C7')
# Grille horizontale uniquement
ax.grid(True, linestyle='--', alpha=0.4, axis='y')
# --- 5. TITRE ET LABELS ---
ax.set_title('DISTRIBUTION DES DONNÉES', loc='center', fontsize=16, fontweight='bold', color='#2C3E50', pad=20)
ax.set_xlabel('Valeurs mesurées', color='#7F8C8D')
ax.set_ylabel('Nombre d\'individus', color='#7F8C8D')
plt.tight_layout()
plt.show()
#Si on veut definir la taille des bordure on crees mes bordures=[0, 5, 10, 15, 20] et on fais bin=mes bordures"""
# ==========================================
#Diagramme en barre
# ==========================================
#DONNÉES (Catégories et Valeurs)
"""categories = ['Produit A', 'Produit B', 'Produit C', 'Produit D']
valeurs = [15, 24, 12, 18]
#CRÉATION DU CADRE ET DU DESSIN
# Fond gris très clair (#F8F9FA)
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#F8F9FA')
ax.set_facecolor('#F8F9FA')
#TRACÉ DU DIAGRAMME EN BARRES
# On utilise ax.bar pour les catégories
barres = ax.bar(categories, 
                valeurs, 
                color='#1A5276', # Bleu foncé
                edgecolor='#1A5276', # Bordure identique pour un look solide
                linewidth=1,
                width=0.6, # Largeur des barres (0.6 laisse un bel espace)
                alpha=0.9)
#NETTOYAGE ET STYLE 
# On enlève les bordures inutiles
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False) # On enlève aussi la gauche pour plus de modernité
ax.spines['bottom'].set_color('#BDC3C7')
# Grille horizontale pour aider la lecture des valeurs
ax.grid(axis='y', linestyle='--', alpha=0.4)
#TITRE ET LABELS
ax.set_title('COMPARAISON PAR CATÉGORIE', loc='left', fontsize=16, fontweight='bold', color='#2C3E50', pad=25)
ax.tick_params(axis='x', colors='#7F8C8D', labelsize=11)
ax.tick_params(axis='y', colors='#7F8C8D')
# Optionnel : Ajouter les chiffres au-dessus de chaque barre
for barre in barres:
    hauteur = barre.get_height()
    ax.annotate(f'{hauteur}',
                xy=(barre.get_x() + barre.get_width() / 2, hauteur),
                xytext=(0, 5), # 5 points de décalage vers le haut
                textcoords="offset points",
                ha='center', va='bottom', 
                fontsize=10, fontweight='bold', color='#1A5276')
plt.tight_layout()
plt.show()"""
# ==========================================
#Camembert
# ==========================================
#DONNÉES
"""labels = ['Ventes A', 'Ventes B', 'Ventes C', 'Ventes D']
tailles = [35, 25, 25, 15] # Le total doit faire 100 idéalement
# Couleurs modernes (une palette de bleus/gris)
couleurs = ['#1A5276', '#2980B9', '#AED6F1', '#D6DBDF']
#CRÉATION DU CADRE 
fig, ax = plt.subplots(figsize=(8, 8), facecolor='#F8F9FA')
#TRACÉ DU CAMEMBERT 
wedges, texts, autotexts = ax.pie(
    tailles, 
    labels=labels, 
    autopct='%1.1f%%', # Affiche le pourcentage (ex: 25.0%)
    startangle=90, # Fait pivoter le graphique pour le style
    colors=couleurs, 
    radius=1.1,
    pctdistance=0.85, # Distance du texte par rapport au centre
    explode=(0.05, 0, 0, 0), # "Sort" légèrement la première part pour la mettre en avant
    wedgeprops={'edgecolor': '#F8F9FA', 'linewidth': 2} # Bordures entre les parts
)
#L'ASTUCE DU "DONUT" (LE TROU AU MILIEU) 
centre_du_cercle = plt.Circle((0,0), 0.70, fc='#F8F9FA') # Un cercle de la couleur du fond
fig.gca().add_artist(centre_du_cercle)
#STYLE DU TEXTE
plt.setp(autotexts, size=10, weight="bold", color="white") # Pourcentages en blanc et gras
plt.setp(texts, size=12, color="#2C3E50") # Libellés en gris foncé
ax.set_title("RÉPARTITION DES VENTES", fontsize=16, fontweight='bold', color='#2C3E50', pad=20)
plt.tight_layout()
plt.show()"""
# ==========================================
#Boxplot
# ==========================================
#TES DONNÉES
# On simule trois groupes de données (ex: scores de 3 classes différentes)
classe_A = np.random.normal(12, 3, 100)
classe_B = np.random.normal(10, 2, 100)
classe_C = np.random.normal(15, 4, 100)
donnees = [classe_A, classe_B, classe_C]
noms_groupes = ['Classe A', 'Classe B', 'Classe C']
#CRÉATION DU CADRE 
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#F8F9FA')
ax.set_facecolor('#F8F9FA')
#TRACÉ DE LA BOXPLOT 
# patch_artist=True permet de remplir l'intérieur des boîtes avec de la couleur
bp = ax.boxplot(donnees, 
                patch_artist=True, 
                labels=noms_groupes,
                notch=True, # Ajoute une encoche au niveau de la médiane
                widths=0.6) # Largeur des boîtes
#STYLE PERSONNALISÉ 
#On change les couleurs pour que ce soit stylé
for box in bp['boxes']:
    box.set(facecolor='#AED6F1', color='#1A5276', linewidth=2) # Bleu clair, contour bleu foncé
for whisker in bp['whiskers']:
    whisker.set(color='#1A5276', linewidth=2, linestyle='--') # Les moustaches en pointillés
for median in bp['medians']:
    median.set(color='#E74C3C', linewidth=3) # La ligne de la médiane en rouge épais
#NETTOYAGE
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#BDC3C7')
ax.grid(axis='y', linestyle='--', alpha=0.3)
ax.set_title("ANALYSE DES SCORES PAR CLASSE", loc='left', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()








