import pandas as pd

# Création des données fictives
data = {
    'Nom Client': ['Société Alpha', 'Cabinet Beta', 'Jean Dupont', 'Tech Solutions'],
    'Mois': ['Janvier 2024', 'Janvier 2024', 'Février 2024', 'Mars 2024'],
    'Montant': [1500.00, 450.50, 2000.00, 3200.75],
    'Reference': ['REF-001', 'REF-002', 'REF-003', 'REF-004']
}

# Création du DataFrame et export Excel
df = pd.DataFrame(data)
df.to_excel('donnees_clients.xlsx', index=False)

print("✅ Fichier 'donnees_clients.xlsx' généré avec succès.")
