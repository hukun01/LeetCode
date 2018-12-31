class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        Binary-search for where the resulting elements start in the array. 
        It's the first index i so that arr[i] is better than arr[i+k] 
        (with "better" meaning closer to or equally close to x). 
        Then just return the k elements starting there.
        
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l, h = 0, len(arr) - k
        while l < h:
            m = (l + h) // 2
            if abs(arr[m] - x) > abs(arr[m + k] - x):
                l = m + 1
            else:
                # If there is a tie, the smaller elements are always preferred.
                # Hence we reduce h.
                h = m
        return arr[l:l + k]