def verifier_suffisance(df, col_hat_r, col_y, col_a, tolerance=0.05):
    # 1. Précision (PPV) : P(Y=1 | R_hat=1)
    df_r1 = df[df[col_hat_r] == 1]
    ppv_a0 = df_r1[df_r1[col_a] == 0][col_y].mean()
    ppv_a1 = df_r1[df_r1[col_a] == 1][col_y].mean()
    
    # 2. Valeur Prédictive Négative (NPV) : P(Y=1 | R_hat=0)
    # (Note : on regarde souvent si P(Y=0 | R_hat=0) est égal, ce qui revient au même)
    df_r0 = df[df[col_hat_r] == 0]
    npv_a0 = df_r0[df_r0[col_a] == 0][col_y].mean()
    npv_a1 = df_r0[df_r0[col_a] == 1][col_y].mean()
    
    diff_ppv = abs(ppv_a0 - ppv_a1)
    diff_npv = abs(npv_a0 - npv_a1)

    is_sufficient = diff_ppv <= tolerance and diff_npv <= tolerance
    
    return (ppv_a0, ppv_a1, npv_a0, npv_a1, diff_ppv, diff_npv, is_sufficient)