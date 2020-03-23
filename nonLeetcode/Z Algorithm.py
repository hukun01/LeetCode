def zAlgorithm(T):
    '''
    Z algorithm is used to do string matching, it's simpler than KMP.

    Giving a string T, Z algo helps us find an array of Z values in which
    each index i represents the longest prefix length when comparing T[i:] and T.
    '''
    L = R = 0
    Z = [0] * len(T)
    Z[0] = len(T)
    for i in range(1, len(T)):
        if i > R:
            L = R = i
            while R < len(T) and T[R] == T[R - L]:
                R += 1
            R -= 1
            Z[i] = R - L + 1
        else:
            k = i - L
            if Z[k] < R - i + 1:
                Z[i] = Z[k]
            else:
                L = i
                while R < len(T) and T[R] == T[R - L]:
                    R += 1
                R -= 1
                Z[i] = R - L + 1
    return sum(Z)