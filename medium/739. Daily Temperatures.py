# 739. Daily Temperatures
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        '''
        Monotonic stack
        Store the index of the previous temperatures in a stack, when seeing
        a new temperature t, if last temperature < t, pop stack and mark that
        previous index using the current distance.

        Time: O(n) where n is len(T)
        Space: O(n)
        '''
        prev_temp_idx = []
        ans = [0] * len(T)
        for i, t in enumerate(T):
            while prev_temp_idx and T[prev_temp_idx[-1]] < t:
                prev_i = prev_temp_idx.pop()
                ans[prev_i] = i - prev_i
            prev_temp_idx.append(i)
        return ans