# 768. Max Chunks To Make Sorted II
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        '''
        Scan through the array.
        Intuition: At an index i, if all numbers before i are less than
        all numbers after i, then the left numbers can form a chunk.
        '''
        n = len(arr)
        rightMin = [0] * n
        rightMin[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            rightMin[i] = min(arr[i], rightMin[i + 1])
        ans = 1
        leftMax = -math.inf
        for i in range(n - 1):
            leftMax = max(leftMax, arr[i])
            if leftMax <= rightMin[i + 1]:
                ans += 1
        return ans