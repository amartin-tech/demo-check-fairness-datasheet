import pandas as pd
from metrics.independance import verifier_independance
from metrics.separation import verifier_separation
from metrics.suffisance import verifier_suffisance

# Exemple d'utilisation :
# A = 0 : FEMME
# A = 1 : HOMME
# R = X : Prediction d'accord de pret 1 OK ; 0 NOK
data = {
    'A': [1,1,1,1,1,0,0,0,0,0],
    'R': [1,1,1,0,0,1,1,1,0,0]
}
df_exemple = pd.DataFrame(data)

df = pd.read_json('dataset.json')

a0, a1, difference, sont_independants = verifier_independance(df, 'R_hat', 'A')
print("# Independance #")
print("Pourcentage femme : " + str(a0))
print("Pourcentage homme : " + str(a1))
print("Difference : " + str(difference))
print("Indépendants : " + str(sont_independants))
#
print("# Separation #")
tpr_a0, tpr_a1, fpr_a0, fpr_a1, diff_tpr, diff_fpr, is_separated = verifier_separation(df, 'R_hat', 'Y', 'A')
print("Taux de Vrais Positifs (TPR) : " + str(tpr_a0))
print("Taux de Faux Positifs (FPR) : " + str(fpr_a0))
print("Difference TPR : " + str(diff_tpr))
print("Difference FPR : " + str(diff_fpr))
print("Séparés : " + str(is_separated))

print("# Suffisance #")
ppv_a0, ppv_a1, npv_a0, npv_a1, diff_ppv, diff_npv, is_sufficient = verifier_suffisance(df, 'R_hat', 'Y', 'A')
print("Précision (PPV) : " + str(ppv_a0))
print("Valeur Prédictive Négative (NPV) : " + str(npv_a0))
print("Difference PPV : " + str(diff_ppv))
print("Difference NPV : " + str(diff_npv))
print("Suffisants : " + str(is_sufficient))