# 1531. String Compression II
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        '''
        Memoized DFS.
        '''
        @lru_cache(None)
        def get_len(idx, prev_char, count, k_remain):
            if k_remain < 0:
                return math.inf
            if idx >= len(s):
                return 0
            if s[idx] == prev_char:
                incr = 1 if count == 1 or count == 9 or count == 99 else 0

                # Always keep s[idx] when it's the same as prev_char,
                # because deleting a char in the middle of
                # the same chars is equivalent to deleting it at the front.
                # And we already explored that option in the below 'else'.
                return incr + get_len(idx+1, prev_char, count+1, k_remain)
            else:
                # Keep s[idx] or delete it
                return min(
                    1 + get_len(idx+1, s[idx], 1, k_remain),
                    get_len(idx+1, prev_char, count, k_remain-1))

        return get_len(0, "", 0, k)