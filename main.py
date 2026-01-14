import pandas as pd
from docxtpl import DocxTemplate
from docx2pdf import convert
import os
from pathlib import Path
from datetime import datetime  

# --- CONFIGURATION ---
INPUT_EXCEL = "donnees_clients.xlsx"
TEMPLATE_WORD = "modele_attestation.docx"
OUTPUT_DIR = Path("Sortie_Attestations")

def setup_dossiers():
    if not OUTPUT_DIR.exists():
        OUTPUT_DIR.mkdir()

def generer_documents():
    try:
        df = pd.read_excel(INPUT_EXCEL)
        print(f"📂 Chargement de {len(df)} lignes depuis {INPUT_EXCEL}...")
    except FileNotFoundError:
        print(f"❌ Erreur : Le fichier {INPUT_EXCEL} est introuvable.")
        return

    setup_dossiers()

    # On récupère la date du jour une seule fois au format JJ/MM/AAAA
    date_actuelle = datetime.now().strftime("%d/%m/%Y")

    for index, row in df.iterrows():
        try:
            client = row['Nom Client']
            mois = row['Mois']
            ref = row['Reference']
            montant = f"{row['Montant']:,.2f}".replace(",", "X").replace(".", ",").replace("X", " ")

            # Ajout de 'date_jour' dans le dictionnaire
            context = {
                'nom_client': client,
                'mois': mois,
                'montant': montant,
                'reference': ref,
                'date_jour': date_actuelle  # <--- La nouvelle variable injectée
            }

            dossier_mois = OUTPUT_DIR / mois
            if not dossier_mois.exists():
                dossier_mois.mkdir(parents=True)

            nom_fichier_base = f"Attestation_{client.replace(' ', '_')}_{ref}"
            chemin_word = dossier_mois / f"{nom_fichier_base}.docx"
            chemin_pdf = dossier_mois / f"{nom_fichier_base}.pdf"

            doc = DocxTemplate(TEMPLATE_WORD)
            doc.render(context)
            doc.save(chemin_word)
            
            convert(str(chemin_word), str(chemin_pdf))

            print(f"✅ Généré : {client} ({mois})")

        except Exception as e:
            print(f"⚠️ Erreur pour le client {client} : {e}")

    print("\n🎉 Traitement terminé !")

if __name__ == "__main__":
    generer_documents()
