import pandas as pd
from metrics.independance import verifier_independance
from metrics.separation import verifier_separation
from metrics.suffisance import verifier_suffisance
from graphs.independance import creer_graphique_independance
from graphs.separation import creer_graphique_separation
from graphs.suffisance import creer_graphique_suffisance


# Exemple d'utilisation :
# A = 0 : FEMME
# A = 1 : HOMME
# R = X : Prediction d'accord de pret 1 OK ; 0 NOK
'''
data = {
    'A': [1,1,1,1,1,0,0,0,0,0],
    'R': [1,1,1,0,0,1,1,1,0,0]
}
df = pd.DataFrame(data)
'''
df = pd.read_json('dataset_suffisance.json')

print("# Dataset #\n")
print("Nombre de d'homme :" + str(len(df[df['A'] == 1])))
print("Nombre de femme :" + str(len(df[df['A'] == 0])))


a0, a1, difference, sont_independants = verifier_independance(df, 'R', 'A')
print("\n# Independance #")
print("Pourcentage femme : " + str(a0))
print("Pourcentage homme : " + str(a1))
print("Difference : " + str(difference))
print("Indépendants : " + str(sont_independants))
#
print("\n# Separation #")
taux_vrai_positif_a0, taux_vrai_positif_a1, taux_faux_positif_a0, taux_faux_positif_a1,diff_taux_vrai_positif, diff_faux_positif, is_separated = verifier_separation(df, 'R', 'Y', 'A')
print("Taux de Vrais Positifs femme : " + str(taux_vrai_positif_a0))
print("Taux de Vrais Positifs homme : " + str(taux_vrai_positif_a1))
print("Taux de Faux Positifs femme : " + str(taux_faux_positif_a0))
print("Taux de Faux Positifs homme : " + str(taux_faux_positif_a1))
print("Difference homme/femme vrais positifs : " + str(diff_taux_vrai_positif))
print("Difference homme/femme faux positifs: " + str(diff_faux_positif))
print("Résultat metrique séparation : " + str(is_separated))

print("\n# Suffisance #")
precision_positive_a0, precision_positive_a1, precision_negative_a0, precision_negative_a1, diff_precision_positive, diff_precision_negative, is_sufficient = verifier_suffisance(df, 'R', 'Y', 'A')
print("Précision positive femme : " + str(precision_positive_a0))
print("Précision positive homme : " + str(precision_positive_a1))
print("Précision négative femme : " + str(precision_negative_a0))
print("Précision négative homme : " + str(precision_negative_a1))
print("Difference précision positive : " + str(diff_precision_positive))
print("Difference précision négative : " + str(diff_precision_negative))
print("Suffisants : " + str(is_sufficient))

creer_graphique_independance(df)
creer_graphique_separation(df)
creer_graphique_suffisance(df)