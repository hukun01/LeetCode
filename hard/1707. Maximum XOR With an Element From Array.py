# 1707. Maximum XOR With an Element From Array
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        '''
        Bit-wise trie + sort.
        Sort the queries by 'm', for all numbers <= m, add them to the bit-wise
        trie. Then query the trie and greedily find the max possible xor
        between x and any of the existing numbers in trie.

        Time: O(n log(n) + q log(q)) where n is len(nums), q is len(queries).
              The trie add() and query() takes O(32) time each time, so
              overall it adds O(32n + 32q), which is dominated by sort() time.
        Space: O(n + q)

        Similar to
        421. Maximum XOR of Two Numbers in an Array, regarding Trie operations.
        1697. Checking Existence of Edge Length Limited Paths, regarding sort.
        '''
        queries = sorted(enumerate(queries), key=lambda q: q[1][1])
        nums.sort()
        nums_idx = 0
        n = len(nums)
        ans = [0] * len(queries)

        Trie = lambda: defaultdict(Trie)
        trie = Trie()

        def add(num):
            node = trie
            for i in range(31, -1, -1):
                i_th_bit = (num >> i) & 1
                node = node[i_th_bit]

        def query(num):
            node = trie
            if not trie:
                return -1
            max_xor_num = 0
            for i in range(31, -1, -1):
                i_th_bit = (num >> i) & 1
                if (i_th_bit ^ 1) in node:
                    max_xor_num |= (1 << i)
                    node = node[i_th_bit ^ 1]
                else:
                    node = node[i_th_bit]
            return max_xor_num

        for q_i, (x, m) in queries:
            while nums_idx < n and nums[nums_idx] <= m:
                add(nums[nums_idx])
                nums_idx += 1
            ans[q_i] = query(x)
        return ans