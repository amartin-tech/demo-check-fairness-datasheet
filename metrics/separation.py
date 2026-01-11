def verifier_separation(df, col_r, col_y, col_a, tolerance=0.05):
    # 1. Taux de Vrais Positifs (TPR) : P(R=1 | Y=1)
    # Reminder : A = 0 FEMME, A = 1 HOMME
    df_y1 = df[df[col_y] == 1]
    taux_vrai_positif_a0 = df_y1[df_y1[col_a] == 0][col_r].mean()
    taux_vrai_positif_a1 = df_y1[df_y1[col_a] == 1][col_r].mean()
    
    # 2. Taux de Faux Positifs (FPR) : P(R=1 | Y=0)
    df_y0 = df[df[col_y] == 0]
    taux_faux_positif_a0 = df_y0[df_y0[col_a] == 0][col_r].mean()
    taux_faux_positif_a1 = df_y0[df_y0[col_a] == 1][col_r].mean()
    
    diff_taux_vrai_positif = abs(taux_vrai_positif_a0 - taux_vrai_positif_a1)
    diff_faux_positif = abs(taux_faux_positif_a0 - taux_faux_positif_a1)

    is_separated = diff_taux_vrai_positif <= tolerance and \
    diff_faux_positif <= tolerance

    return (taux_vrai_positif_a0, taux_vrai_positif_a1, taux_faux_positif_a0,
            taux_faux_positif_a1,diff_taux_vrai_positif,diff_faux_positif,is_separated)

# VRAI POSITIF : Personne qui est bon payeur ou "solvable" Y=1 et prediction R=1
# FAUX POSITIF : Personne qui est mauvais payeur ou "non solvable" Y=0 et prediction R=1