# 1574. Shortest Subarray to be Removed to Make Array Sorted
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        '''
        Two pointers.
        Find the left sorted prefix, and the right sorted suffix.
        Use these two pointers to locate the middle subarray that
        needs to be removed. Need to ensure prefix[-1] <= suffix[0].
        '''
        n = len(arr)
        left = 0
        while left+1 < n and arr[left] <= arr[left+1]:
            left += 1
        if left == n - 1:
            return 0
        right = n - 1
        while right > left and arr[right-1] <= arr[right]:
            right -= 1
        remove = min(n - 1 - left, right)
        i = 0
        j = right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                remove = min(remove, j - i - 1)
                i += 1
            else:
                j += 1
        return remove