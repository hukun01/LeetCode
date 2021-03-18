# 697. Degree of an Array
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        '''
        Hashmap.
        Find out the degree using a Counter.
        Now the key is to handle the case in which there are multiple elements
        that have the same degrees.
        Use a dict to track the left position for every element, and use a dict
        to track the right position. Now go through nums again, and if an
        element's frequency == degree, we check its left and right position to
        determine the subarray length.

        Time: O(n) where n is len(nums)
        Space: O(n)
        '''
        left = {}
        right = {}
        for i, a in enumerate(nums):
            if a not in left:
                left[a] = i
            right[a] = i

        freqs = Counter(nums)
        degree = max(freqs.values())
        ans = len(nums)
        for a in nums:
            if freqs[a] == degree:
                ans = min(ans, right[a] - left[a] + 1)

        return ans