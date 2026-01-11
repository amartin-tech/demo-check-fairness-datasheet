def verifier_separation(df, col_hat_r, col_y, col_a, tolerance=0.05):
    # 1. Taux de Vrais Positifs (TPR) : P(R_hat=1 | Y=1)
    df_y1 = df[df[col_y] == 1]
    tpr_a0 = df_y1[df_y1[col_a] == 0][col_hat_r].mean()
    tpr_a1 = df_y1[df_y1[col_a] == 1][col_hat_r].mean()
    
    # 2. Taux de Faux Positifs (FPR) : P(R_hat=1 | Y=0)
    df_y0 = df[df[col_y] == 0]
    fpr_a0 = df_y0[df_y0[col_a] == 0][col_hat_r].mean()
    fpr_a1 = df_y0[df_y0[col_a] == 1][col_hat_r].mean()
    
    diff_tpr = abs(tpr_a0 - tpr_a1)
    diff_fpr = abs(fpr_a0 - fpr_a1)

    is_separated = diff_tpr <= tolerance and diff_fpr <= tolerance

    return (tpr_a0, tpr_a1, fpr_a0, fpr_a1, diff_tpr, diff_fpr, is_separated)