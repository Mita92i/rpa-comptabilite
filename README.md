# 🏦 Automatisation de Documents Comptables (RPA)

Ce projet est une solution d'automatisation destinée aux experts-comptables et services administratifs. Il permet de transformer un listing de paiements Excel en documents officiels (Word & PDF) parfaitement mis en forme et classés.

## 📈 Impact Business

- **Gain de temps :** Traitement de 100 attestations en quelques secondes au lieu de plusieurs heures.
- **Zéro Erreur :** Élimine les fautes de frappe lors du copier-coller entre Excel et Word.
- **Organisation :** Archivage automatique et normalisé des fichiers par mois de facturation.

## ⚙️ Fonctionnement Technique

1. **Extraction :** Lecture des données via `pandas`.
2. **Mise en page :** Injection dynamique des données dans un template Word (`docxtpl`) respectant la charte graphique.
3. **Conversion :** Transformation en PDF (`docx2pdf`) pour garantir l'intégrité du document.
4. **Gestion de fichiers :** Création dynamique de l'arborescence des dossiers avec `pathlib`.

## 🛠️ Installation & Utilisation

```bash
# Installation des librairies
pip install pandas openpyxl docxtpl docx2pdf

# Utilisation
1. Remplir le fichier 'donnees_clients.xlsx'
2. Placer le logo dans 'modele_attestation.docx'
3. Lancer 'python script_automatisation.py'
```
