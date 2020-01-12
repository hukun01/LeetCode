# 658. Find K Closest Elements
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Binary-search for where the resulting elements start in the array. 
        It's the first index i so that arr[i] is better than arr[i+k] 
        (with "better" meaning closer to or equally close to x). 
        Then just return the k elements starting there.

        Note that we can't use abs() to get the diffs or it will fail in below case:
        [1,1,2,2,2,3,3], k = 2, x = 3
        The order of x and arr[m] in the diff calculation should be clear if we list out
        all possible cases:
        1. x, arr[mid], arr[mid + k]
        2. arr[mid], x, arr[mid + k]
        3. arr[mid], arr[mid + k], x
        """
        l, h = 0, len(arr) - k
        while l < h:
            m = (l + h) // 2
            if x - arr[m] <= arr[m + k] - x:
                h = m
            else:
                l = m + 1
        return arr[l:l + k]