class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        
        An application of the next permutation. See 31. Next Permutation
        """
        s = list(str(n))
        # 1/4 step: find the first smaller-than-previous element
        i = len(s) - 2
        while i >= 0 and int(s[i]) >= int(s[i + 1]):
            i -= 1
        if i < 0:
            return -1
        # 2/4 step: find the smallest element that is larger than the found one from last step
        j = len(s) - 1
        while int(s[j]) <= int(s[i]):
            j -= 1
        # 3/4 step: swap them
        s[i], s[j] = s[j], s[i]
        # 4/4 step: reverse the right part of the swap point
        s[i + 1 :] = reversed(s[i + 1 :])

        val = int("".join(s))
        return val if val <= ((1<<31) - 1) else -1