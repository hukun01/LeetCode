# 1320. Minimum Distance to Type a Word Using Two Fingers
class Solution:
    def minimumDistance(self, word: str) -> int:
        '''
        1/2 Straightforward DFS with memoization. Note that we should use the 
        letter to represent finger position, instead of using the index, 
        because there are only 26 letters.
        '''
        letters = {}
        for i, l in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            row = i // 6
            col = i % 6
            letters[l] = (row, col)
        
        def distance(char1, char2):
            if char1 == None or char2 == None:
                return 0
            r1, c1 = letters[char1]
            r2, c2 = letters[char2]
            return abs(r1 - r2) + abs(c1 - c2)
        cache = {}
        
        def dfs(f1, f2, i):
            if i == len(word):
                return 0
            if (f1, f2, i) in cache:
                return cache[(f1, f2, i)]
            d1 = distance(f1, word[i]) + dfs(word[i], f2, i + 1)
            d2 = distance(f2, word[i]) + dfs(f1, word[i], i + 1)
            cache[(f1, f2, i)] = min(d1, d2)
            return cache[(f1, f2, i)]
        
        return dfs(None, None, 0)

        '''
        2/2 Note that we only need to keep track of the 'other' finger,
        because the last finger will always be at word[i - 1]. This is much
        faster as the cache space gets reduced from 3D to 2D.
        In this solution, we start i from 1, namely the 0-th char has been
        typed by the 'last' finger before we start DFS.
        '''
        def dfs(other, i):
            if i == len(word):
                return 0
            if (other, i) in cache:
                return cache[(other, i)]
            to = word[i]
            last = word[i - 1]
            d1 = distance(other, to) + dfs(last, i + 1)
            d2 = distance(last, to) + dfs(other, i + 1)
            cache[(other, i)] = min(d1, d2)
            return cache[(other, i)]
        
        return dfs(None, 1)