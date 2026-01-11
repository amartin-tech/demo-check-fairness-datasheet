def verifier_independance(df, col_r, col_a, tolerance=0.05):
    """
    Vérifie si P(R=1 | A=0) est approximativement égal à P(R=1 | A=1)
    """
    # Calcul de P(R=1 | A=0)
    p_r1_a0 = df[df[col_a] == 0][col_r].mean()
    
    # Calcul de P(R=1 | A=1)
    p_r1_a1 = df[df[col_a] == 1][col_r].mean()
    
    difference = abs(p_r1_a0 - p_r1_a1)
    sont_independants = difference <= tolerance

    return (p_r1_a0, p_r1_a1, difference, sont_independants)