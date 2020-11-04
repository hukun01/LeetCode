# 628. Maximum Product of Three Numbers
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        '''
        If there is no negative numbers in the biggest 3, apparently
        the biggest 3 will be used for product.
        If there are negative numbers in the biggest 3, the smallest 2
        numbers must all be negative, then biggest1 * smallest1 * smallest2
        is the max product.
        If all biggest 3 are negative, the biggest 3 will still make
        the biggest product.

        Use heapq.nlargest and heapq.nsmallest.
        '''
        b1, b2, b3 = heapq.nlargest(3, nums)
        s1, s2 = heapq.nsmallest(2, nums)
        return max(b1 * b2 * b3, b1 * s1 * s2)