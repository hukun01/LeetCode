# 1220. Count Vowels Permutation
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        maps = {
            'x': 'aeiou',
            'a': 'e',
            'e': 'ai',
            'i': 'aeou',
            'o': 'iu',
            'u': 'a'
        }
        
        @lru_cache(None)
        def dfs(lastChar, currLen):
            if currLen == n:
                return 1

            total = 0
            for c in maps[lastChar]:
                total += dfs(c, currLen + 1)
            return total

        return dfs('x', 0) % (10 ** 9 + 7)
    '''
    v represents the number of paths starting with each vowel.
    Initially it's all 1, meaning that there is 1 path starting with every char.
    In n-1 iterations, for a specific char, like 'a', the number of possible
    paths after 'a' is the number of paths starting with 'e'. Similarly, the number
    of possible paths after 'e' is the number of paths starting with 'a' and 'i'.
    And so on.
    '''
    '''
        v = [1]*5
        for _ in range(n-1):
            w = [0]*5
            w[0] = v[1]
            w[1] = v[0]+v[2]
            w[2] = v[0]+v[1]+v[3]+v[4]
            w[3] = v[2]+v[4]
            w[4] = v[0]
            v = w
        return sum(v) % (10**9+7)
    '''