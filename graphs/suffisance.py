import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Calcul des métriques de Suffisance (Calibration)
# PPV (Positive Predictive Value) : P(Y=1 | R=1) -> "Parmi ceux acceptés, combien le méritaient ?"
# FOR (False Omission Rate) : P(Y=1 | R=0) -> "Parmi ceux rejetés, combien méritaient d'être acceptés ?"

def get_sufficiency(dataframe, group_val):
    subset = dataframe[dataframe['A'] == group_val]
    
    # Précision : P(Y=1 | R=1)
    accepted = subset[subset['R'] == 1]
    ppv = accepted['Y'].mean() if len(accepted) > 0 else 0
    
    # Omission : P(Y=1 | R=0)
    rejected = subset[subset['R'] == 0]
    for_rate = (1 - rejected['Y']).mean() if len(rejected) > 0 else 0
    
    return ppv, for_rate

# Ajout des étiquettes de valeur
def autolabel(rects, ax):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), # 3 points de décalage vertical
                    textcoords="offset points",
                    ha='center', va='bottom', fontweight='bold')


def creer_graphique_suffisance(data):

    # Chargement et nettoyage des données
    df = pd.DataFrame(data)

    # Nettoyage : fusionner la clé alternative '0' vers 'Y' si elle existe
    if '0' in df.columns:
        df['Y'] = df['Y'].fillna(df['0'])
        df.drop(columns=['0'], inplace=True)

    ppv0, for0 = get_sufficiency(df, 0)
    ppv1, for1 = get_sufficiency(df, 1)

    # 4. Visualisation
    labels = ['Précision positive', "Précision négative"]
    a0_values = [ppv0, for0]
    a1_values = [ppv1, for1]

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar(x - width/2, a0_values, width, label='Groupe A=0', color='#3498db')
    rects2 = ax.bar(x + width/2, a1_values, width, label='Groupe A=1', color='#e74c3c')

    # Stylisation
    ax.set_ylabel('Proportion')
    ax.set_title('Représentation de la Suffisance (Calibration)')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 1.1)
    ax.legend()

    autolabel(rects1, ax)
    autolabel(rects2, ax)

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('suffisance_plot.png')
