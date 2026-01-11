def verifier_suffisance(df, col_r, col_y, col_a, tolerance=0.05):
    # 1. Précision (PPV) : P(Y=1 | R=1)
    df_r1 = df[df[col_r] == 1]
    precision_positive_a0 = df_r1[df_r1[col_a] == 0][col_y].mean()
    precision_positive_a1 = df_r1[df_r1[col_a] == 1][col_y].mean()
    
    # 2. Valeur Prédictive Négative (NPV) : P(Y=1 | R=0)
    # (Note : on regarde souvent si P(Y=0 | R_hat=0) est égal, ce qui revient au même)
    df_r0 = df[df[col_r] == 0]
    precision_negative_a0 = df_r0[df_r0[col_a] == 0][col_y].mean()
    precision_negative_a1 = df_r0[df_r0[col_a] == 1][col_y].mean()
    
    diff_precision_positive = abs(precision_positive_a0 - precision_positive_a1)
    diff_precision_negative = abs(precision_negative_a0 - precision_negative_a1)

    is_sufficient = diff_precision_positive <= tolerance and \
        diff_precision_negative <= tolerance
    
    return (precision_positive_a0, precision_positive_a1, precision_negative_a0,
            precision_negative_a1, diff_precision_positive, diff_precision_negative,
            is_sufficient)