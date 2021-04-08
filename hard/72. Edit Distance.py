# 72. Edit Distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        1/3 Memoized DFS.

        Time: O(n^2)
        Space: O(n^2)
        Similar to 10. Regular Expression Matching
        '''
        w1, w2 = word1, word2

        @cache
        def match(i1, i2):
            if i1 == -1:
                return i2 + 1
            if i2 == -1:
                return i1 + 1

            if w1[i1] == w2[i2]:
                return match(i1 - 1, i2 - 1)
            else:
                return min(match(i1, i2 - 1),          # insert to w1[i1]
                           match(i1 - 1, i2),          # delete w1[i1]
                           match(i1 - 1, i2 - 1)) + 1  # replace w1[i1]
        return match(len(w1) - 1, len(w2) - 1)
        '''
        2/3 DP.
        Bottom-up version of 1/3 with possibility to reduce space.

        Let f[i1, i2] be the min distance to convert word1[:i1] to word2[:i2]
        When word1[i1-1] == word2[i2-1]:
            f[i1][i2] = f[i1-1][i2-1]
        Otherwise:
            f[i1][i2] = min(
                f[i1-1][i2] + 1, aka, delete word1[i1] to make word2[i2]
                f[i1][i2-1] + 1, aka, insert after word1[i1] to make word2[i2]
                f[i1-1][i2-1] +1, aka, replace)

        Note that we need to take care of the boundary cases where i1 = 0 or
        i2 = 0.

        Time: O(n^2)
        Space: O(n^2)

        Similar to 1143. Longest Common Subsequence
        '''
        l1, l2 = len(word1), len(word2)
        f = [[inf] * (l2 + 1) for _ in range(l1 + 1)]
        for i1 in range(l1 + 1):
            f[i1][0] = i1
        for i2 in range(l2 + 1):
            f[0][i2] = i2
        for i1 in range(1, l1 + 1):
            for i2 in range(1, l2 + 1):
                if word1[i1-1] == word2[i2-1]:
                    f[i1][i2] = f[i1-1][i2-1]
                else:
                    f[i1][i2] = min(f[i1-1][i2], f[i1][i2-1], f[i1-1][i2-1]) + 1
        return f[l1][l2]
        '''
        3/3 DP with O(n) space.
        Based on 2/3, we know f[i1] only depends on f[i1-1], so we just need 2
        arrays with [i2+1] size, instead of l1 arrays.
        Note that we still need to handle boundary when i2 == 0.
        '''
        l1, l2 = len(word1), len(word2)
        f = list(range(l2 + 1))
        for i1 in range(1, l1 + 1):
            f2 = [0] * (l2 + 1)
            f2[0] = i1
            for i2 in range(1, l2 + 1):
                if word1[i1-1] == word2[i2-1]:
                    f2[i2] = f[i2-1]
                else:
                    f2[i2] = min(f[i2-1], f2[i2-1], f[i2]) + 1
            f = f2
        return f[l2]