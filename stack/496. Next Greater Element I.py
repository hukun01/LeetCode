class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        Since nums1 is a subset of nums2, we just need to traverse nums2 for the below logic.
        We use a stack to keep a decreasing sub-sequence, 
        whenever we see a number n greater than stack.peek(),
        we pop all elements less than n, and for all the popped ones, 
        their next greater element is n.
        We use a dict to cache this result.
        """
        stack = []
        nextGreaters = {}
        for n in nums2:
            while stack and stack[-1] < n:
                nextGreaters[stack.pop()] = n
            stack.append(n)
        return [nextGreaters.get(n, -1) for n in nums1]