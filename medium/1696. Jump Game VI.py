# 1696. Jump Game VI
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        '''
        DP + sliding window maximum.
        Let f[i] be the ans for nums[:i+1]
        f[i] = nums[i] + max(f[j] for all i-k <= j < i)
        Direct implementation of above takes O(n^2) time. We can use a sliding
        window of maximum to track f[j] and retrieve the max one in O(1) time.
        Then the overall time becomes O(n).

        Time: O(n) where n is len(nums).
        Space: O(n) can be reduced to O(k) by replacing f[] with cur_f.

        Similar to 1687. Delivering Boxes from Storage to Ports
        '''
        n = len(nums)
        f = [0] * n
        f[0] = nums[0]
        max_f_idx = deque([0])
        for i in range(1, n):
            f[i] = nums[i] + f[max_f_idx[0]]

            while max_f_idx and f[max_f_idx[-1]] < f[i]:
                max_f_idx.pop()
            max_f_idx.append(i)

            if i - k == max_f_idx[0]:
                max_f_idx.popleft()
        return f[-1]