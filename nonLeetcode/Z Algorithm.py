def zAlgorithm(string):
    '''
    Z algorithm is used to do string matching, it's simpler than KMP, but KMP can
    handle streaming data, while Z cannot.

    Giving a string T, Z algo helps us find an array Z values in which each index i
    represents the longest prefix length when comparing T[i:] and T.
    '''
    L = R = 0
    Z = [0] * len(string)
    Z[0] = len(string)
    for i in range(1, len(string)):
        if i > R:
            L = R = i
            while R < len(string) and string[R] == string[R - L]:
                R += 1
            R -= 1
            Z[i] = R - L + 1
        else:
            k = i - L
            if Z[k] < R - i + 1:
                Z[i] = Z[k]
            else:
                L = i
                while R < len(string) and string[R] == string[R - L]:
                    R += 1
                R -= 1
                Z[i] = R - L + 1
    return sum(Z)