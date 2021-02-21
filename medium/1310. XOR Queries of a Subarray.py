# 1310. XOR Queries of a Subarray
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        '''
        Prefix array.
        Note that xor in [a, b] = [0, b] ^ [0, a-1], so we can pre-compute all
        [0, i] with a prefix array, and answer each query in O(1) time.

        Time: O(n + q) where n is len(arr), q is len(queries)
        Space: O(n + q)
        '''
        n = len(arr)
        prefix_xors = [0] * (n + 1)
        for i in range(n):
            prefix_xors[i+1] = prefix_xors[i] ^ arr[i]
        return [prefix_xors[r+1] ^ prefix_xors[l] for l, r in queries]