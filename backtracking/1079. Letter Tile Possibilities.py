class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        '''
        It's critical to keep the word-count for all characters.
        '''
        letters = collections.Counter(tiles)
        def dfs():
            total = 0
            for l, count in letters.items():
                if count == 0:
                    continue
                total += 1
                letters[l] -= 1
                total += dfs()
                letters[l] += 1
            return total
        return dfs()