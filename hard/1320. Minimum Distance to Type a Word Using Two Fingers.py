# 1320. Minimum Distance to Type a Word Using Two Fingers
class Solution:
    def minimumDistance(self, word: str) -> int:
        '''
        1/2 Straightforward DFS with memoization. Note that we should use the
        letter to represent finger position, instead of using the index, 
        because there are only 26 letters.

        Time: O(n^3) where n is len(word)
        Space: O(n^3)
        '''
        C = 6
        letters = {}
        for i, l in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            row = i // C
            col = i % C
            letters[l] = (row, col)

        def distance(char1, char2):
            if char1 == None or char2 == None:
                return 0
            r1, c1 = letters[char1]
            r2, c2 = letters[char2]
            return abs(r1 - r2) + abs(c1 - c2)

        @cache
        def dfs(f1, f2, i):
            if i == len(word):
                return 0
            to = word[i]
            d1 = distance(f1, to) + dfs(to, f2, i + 1)
            d2 = distance(f2, to) + dfs(f1, to, i + 1)
            return min(d1, d2)

        return dfs(None, None, 0)

        '''
        2/2 Note that we only need to keep track of the 'other' finger, because
        the last finger will always be at word[i - 1]. Hence in the dfs() we
        only pass the 'other' to the recursion, and get 'last' from word[i-1].
        Similarly, we start i from 1, namely the 0-th char has been typed by
        the 'last' finger before we start DFS.

        This is much faster as the cache space gets reduced from 3D to 2D.

        Time: O(n^2) where n is len(word)
        Space: O(n^2)
        '''
        C = 6
        letters = {}
        for i, l in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            row = i // C
            col = i % C
            letters[l] = (row, col)

        def distance(char1, char2):
            if char1 == None or char2 == None:
                return 0
            r1, c1 = letters[char1]
            r2, c2 = letters[char2]
            return abs(r1 - r2) + abs(c1 - c2)

        @lru_cache(None)
        def dfs(other, i):
            if i == len(word):
                return 0
            to = word[i]
            last = word[i - 1]
            d1 = distance(other, to) + dfs(last, i + 1)
            d2 = distance(last, to) + dfs(other, i + 1)
            return min(d1, d2)

        return dfs(None, 1)