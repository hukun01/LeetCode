# 421. Maximum XOR of Two Numbers in an Array
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        '''
        Bit-wise Trie.
        Build a bit-wise trie that tracks the 0s and 1s for each number.
        For each number, find the max xor with any of other numbers in trie.
        From left (the most significant) to right bits, at every bit, greedily
        choose the bit that would xor to 1 with the bit of current number.

        Time: O(32n) where n is len(nums)
        Space: O(n)
        '''
        Trie = lambda: defaultdict(Trie)
        root = Trie()
        # Build the trie with nums
        for a in nums:
            node = root
            for i in range(31, -1, -1):
                i_th_bit = (a >> i) & 1
                node = node[i_th_bit]

        ans = 0
        for a in nums:
            node = root
            max_xor_with_a = 0
            for i in range(31, -1, -1):
                i_th_bit = (a >> i) & 1
                if (i_th_bit ^ 1) in node:
                    max_xor_with_a |= (1 << i)
                    node = node[i_th_bit ^ 1]
                else:
                    node = node[i_th_bit]
            ans = max(ans, max_xor_with_a)

        return ans