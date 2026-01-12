import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Calcul des métriques de séparation
def get_separation_metrics(df, group_val):
    subset = df[df['A'] == group_val]
    # TPR : P(R=1 | Y=1)
    tpr = subset[subset['Y'] == 1]['R'].mean()
    # FPR : P(R=1 | Y=0)
    fpr = subset[subset['Y'] == 0]['R'].mean()
    return tpr, fpr

def autolabel(rects, ax):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2%}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontweight='bold')

def creer_graphique_separation(data):

    # Chargement et nettoyage des données
    df = pd.DataFrame(data)

    tpr0, fpr0 = get_separation_metrics(df, 0)
    tpr1, fpr1 = get_separation_metrics(df, 1)

    # Graphique
    labels = ['Vrais Positifs (TPR)', 'Faux Positifs (FPR)']
    group0 = [tpr0, fpr0]
    group1 = [tpr1, fpr1]

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 5))
    rects1 = ax.bar(x - width/2, group0, width, label='Groupe A=0', color='#3498db')
    rects2 = ax.bar(x + width/2, group1, width, label='Groupe A=1', color='#e74c3c')

    ax.set_ylabel('Proportion')
    ax.set_title('Critère de Séparation (Equalized Odds)')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 1)
    ax.legend()

    autolabel(rects1, ax)
    autolabel(rects2, ax)

    plt.savefig('separation_plot.png')