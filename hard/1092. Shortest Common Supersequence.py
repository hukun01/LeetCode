# 1092. Shortest Common Supersequence
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        '''
        Find the LCS str3 between str1 and str2, and the shortest
        common supersequence will be str1-str3-str2 interleavingly.
        '''
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        f0 = [''] * (len(str2) + 1)
        for i in range(1, len(str1) + 1):
            f1 = f0[:]
            for j in range(1, len(str2) + 1):
                if str1[i-1] == str2[j-1]:
                    f1[j] = f0[j-1] + str1[i-1]
                else:
                    if len(f0[j]) < len(f1[j-1]):
                        f1[j] = f1[j-1]
            f0 = f1
        lcs = f0[-1]
        res, i, j = "", 0, 0
        for c in lcs:
            while str1[i] != c:
                res += str1[i]
                i += 1
            while str2[j] != c:
                res += str2[j]
                j += 1
            res += c
            i, j = i + 1, j + 1
        return res + str1[i:] + str2[j:]