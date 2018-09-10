class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        
        This is the same as Interval Scheduling problem. Use greedy.
        """
        if not pairs:
            return 0
        pairs.sort(key=lambda a: a[1])
        count = 1
        pre = pairs[0][1]
        for p in pairs[1:]:
            if p[0] > pre:
                count += 1
                pre = p[1]
        return count