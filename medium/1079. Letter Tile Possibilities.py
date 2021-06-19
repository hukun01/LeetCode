class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        '''
        DFS with word count.

        It's critical to keep the word-count for all characters.

        letters[l] -= 1; means we are using the tile 'l' as the current tile
        because there are still remaining ones.
        total += 1; means with these current tiles we already have a valid
        combination.
        total += dfs(); means if we want to add more tiles to the existing
        combination, we simply do recursion with the tiles left;
        letters[l] += 1; is backtracking because we have finished exploring
        the possibilities of using tile 'l' and need to restore it and continue
        to explore other possibilities.

        Note that, for input like "AAB", we won't have two "AAB" in the result,
        because we are iterating on the keys, which are "AB".
        '''
        counts = Counter(tiles)
        def dfs():
            ans = 0
            for t in counts:
                if counts[t] == 0:
                    continue
                counts[t] -= 1
                ans += dfs() + 1
                counts[t] += 1
            return ans

        return dfs()