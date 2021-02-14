# 853. Car Fleet
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        Sort.
        Sort cars by starting position, then calculate the finish times.
        From right to left, if a car's finish time 't' is greater than 'cur'
        which is the current fleet's finish time, we know the current car is
        slower, so it becomes a new fleet. Otherwise, it can catch up to the
        current fleet and join that.

        Time: O(n log(n))
        Space: O(n)
        '''
        cars = sorted(zip(position, speed))
        times = [(target - p) / s for p, s in cars]
        ans = cur = 0
        for t in reversed(times):
            if t > cur:
                ans += 1
                cur = t
        return ans