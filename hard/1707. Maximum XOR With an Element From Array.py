# 1707. Maximum XOR With an Element From Array
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        '''
        1/2 Bit-wise trie + sort.
        Sort the queries by 'm', for all numbers <= m, add them to the bit-wise
        trie. Then query the trie and greedily find the max possible xor
        between x and any of the existing numbers in trie.

        Time: O(n log(n) + q log(q)) where n is len(nums), q is len(queries).
              The trie add() and query() takes O(32) time each time, so
              overall it adds O(32n + 32q), which may get dominated by sort()
              time if n or q is greater 10^32.
        Space: O(n + q)

        Similar to
        421. Maximum XOR of Two Numbers in an Array, regarding Trie operations.
        1697. Checking Existence of Edge Length Limited Paths, regarding sort.
        '''
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

        queries = sorted(enumerate(queries), key=lambda q: q[1][1])
        nums.sort()
        nums_idx = 0
        n = len(nums)
        ans = [0] * len(queries)

        for q_i, (x, m) in queries:
            while nums_idx < n and nums[nums_idx] <= m:
                add(nums[nums_idx])
                nums_idx += 1
            ans[q_i] = query(x)
        return ans
        '''
        2/2 Sort + binary search.
        Sort the nums, and for each query (x, m), find the best possible
        number within [:bound(m)], which can be located by binary search. The
        best number has the opposite bit at every possible positions, comparing
        to x.
        We start by finding the 'stop' position in nums using 'm'.
        Similar to 1/2, we try from the most significant bit to the least ones.
        During the process, we track the currently identified number from its
        highest bits.
        At each bit, let 'plus' be current number + bit.
            1. if nums[start] >= 'plus', meaning all numbers have this bit set,
               then we have to take it, regardless of x's bit.
            2. If nums[start] < 'plus', meaning it doesn't have this bit set,
               we check whether the larger end, nums[stop - 1], has this bit
               set, if it does, meaning we have a choice to choose a number
               with this bit set or not, based on what x has on this bit:
                a. If x has this bit set, we want to find a number in the
                   smaller half, that has this bit being 0. Hence, discard the
                   larger half.
                b. Otherwise, we want to do the opposite.
            3. If nums[stop - 1] < 'plus', meaning all numbers within range
               doesn't have this bit set, then we can't use it, regardless of
               x's bit.

        Time: O(n log(n) + q log(n))
        Space: O(n + q)
        Note that this solution is much faster than 1/2, althoug the
        theorectical complexity is close. This is because space is much much
        less here, while in 1/2 we need to store up to 2^31 Trie nodes.
        '''
        nums.sort()

        def query(x, m):
            start, stop = 0, bisect_right(nums, m)
            num = 0
            for i in range(31, -1, -1):
                i_th_bit = 1 << i
                plus = num + i_th_bit
                if nums[start] >= plus:
                    num = plus
                elif nums[stop-1] >= plus:
                    cut = bisect_left(nums, plus, start, stop)
                    if x & i_th_bit:
                        stop = cut
                    else:
                        start = cut
                        num = plus
            return num ^ x

        return [query(x, m) if nums[0] <= m else -1 for x, m in queries]