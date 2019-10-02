class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        left, right = 0, len(A)-1
        ans = -1
        while left < right:
            currSum = A[left] + A[right]
            if currSum < K:
                left += 1
                ans = max(ans, currSum)
            else:
                right -= 1
        return ans