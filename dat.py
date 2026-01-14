import pandas as pd
import random

noms_entreprises = [
    "Alpha Compta", "Boulangerie Soleil", "Garage du Centre", "Tech Innovate", 
    "Cabinet Médical Santé", "Restaurant Le Gourmet", "Hôtel de la Plage", 
    "Boutique Mode", "Agence Immo Plus", "Artisan Bois", "Studio Graphique",
    "Coiffeur Style", "Librairie des Arts", "Pressing Éclat", "Fleuriste Rose"
]

mois_liste = ["Janvier 2024", "Février 2024", "Mars 2024"]

data = []

for i in range(1, 41):
    entreprise = random.choice(noms_entreprises) + f" {random.randint(1, 100)}"
    mois = random.choice(mois_liste)
    montant = round(random.uniform(150.0, 5000.0), 2)
    reference = f"PAIE-2024-{i:03d}"
    
    data.append([entreprise, mois, montant, reference])

# Création du DataFrame
df = pd.DataFrame(data, columns=['Nom Client', 'Mois', 'Montant', 'Reference'])

# Export
df.to_excel('donnees_clients.xlsx', index=False)

print(f"✅ Fichier 'donnees_clients.xlsx' avec {len(df)} lignes généré !")
