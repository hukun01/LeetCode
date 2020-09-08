# 1574. Shortest Subarray to be Removed to Make Array Sorted
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        '''
        Two pointers.
        Find the left sorted prefix, and the right sorted suffix.
        Use these two pointers to locate the middle subarray that
        needs to be removed.
        Need to ensure left and right pointers never overlap.
        Need to ensure prefix[-1] <= suffix[0].
        '''
        n = len(arr)
        left = 0
        while left+1 < n and arr[left] <= arr[left+1]:
            left += 1
        right = n - 1
        while right > left and arr[right-1] <= arr[right]:
            right -= 1
        remove = min(n - 1 - left, right)
        l = 0
        r = right
        while l <= left < r < n:
            if arr[l] <= arr[r]:
                remove = min(remove, r - l - 1)
                l += 1
            else:
                r += 1
        return remove