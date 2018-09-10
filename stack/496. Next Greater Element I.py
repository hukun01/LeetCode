class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        We use a stack to keep a decreasing sub-sequence, 
        whenever we see a number x greater than stack.peek(),
        we pop all elements less than x and for all the popped ones, 
        their next greater element is x.
        We use a dict to cache this result.
        """
        stack = []
        nextDict = {}
        for n in nums2:
            while stack and stack[-1] < n:
                nextDict[stack.pop()] = n
            stack.append(n)
        ans = []
        for n in nums1:
            ans.append(nextDict[n] if n in nextDict else -1)
        return ans