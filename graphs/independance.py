import pandas as pd
import matplotlib.pyplot as plt

def creer_graphique_independance(data):

    # Chargement et nettoyage des données
    df = pd.DataFrame(data)
    if '0' in df.columns:
        df['Y'] = df['Y'].fillna(df['0'])
        df.drop(columns=['0'], inplace=True)

    # Calcul des probabilités de décision positive par groupe
    prob_A0 = df[df['A'] == 0]['R'].mean()
    prob_A1 = df[df['A'] == 1]['R'].mean()

    # Création du graphique
    groups = ['Groupe A=0', 'Groupe A=1']
    proportions = [prob_A0, prob_A1]

    plt.bar(groups, proportions, color=['#3498db', '#e74c3c'])
    plt.axhline(y=prob_A0, color='gray', linestyle='--', alpha=0.6, label='Référence A=0')

    # Mise en forme
    plt.ylabel('Proportion de décisions favorables (R=1)')
    plt.title("Représentation de l'Indépendance (Demographic Parity)")
    plt.ylim(0, 1)

    # Ajout des valeurs sur les barres
    for i, val in enumerate(proportions):
        plt.text(i, val + 0.02, f"{val:.2%}", ha='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig('independance_plot.png')