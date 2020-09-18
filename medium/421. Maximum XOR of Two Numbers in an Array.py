# 421. Maximum XOR of Two Numbers in an Array
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        '''
        Trie.
        From left to right bits, find the max possible prefix by XORing
        the bits from each number with any one of the other numbers seen.
        '''
        L = len(bin(max(nums))) - 2
        # We want to check the more significant bits first, hence the reverse.
        nums = [[(x >> i) & 1 for i in range(L)[::-1]] for x in nums]
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        max_xor = 0
        for num in nums:
            node = trie
            xor_node = trie
            curr_xor = 0
            for bit in num:
                curr_xor <<= 1
                node = node[bit]

                xor_bit = 1 - bit
                if xor_bit in xor_node:
                    curr_xor |= 1
                    xor_node = xor_node[xor_bit]
                else:
                    xor_node = xor_node[bit]
            max_xor = max(max_xor, curr_xor)
        return max_xor