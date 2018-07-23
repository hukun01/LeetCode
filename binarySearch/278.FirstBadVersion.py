# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, h = 1, n
        while l < h:
            m = (l + h) // 2
            # shrinking down the search scope by doing (l, h]
            if isBadVersion(m):
                h = m
            else:
                l = m + 1
        return l