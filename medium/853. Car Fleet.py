# 853. Car Fleet
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        Sort.
        Sort cars by starting position, then calculate the finish times.
        From later positions to earlier ones, if a car's finish time 't' is
        strictly greater than 'cur_time' which is the current fleet's finish
        time, we know the current car is slower, so it becomes a new fleet.
        Otherwise, it can catch up to the current fleet and join that.

        Time: O(n log(n))
        Space: O(n)
        '''
        cars = sorted(zip(position, speed), reverse=True)
        cur_time = ans = 0
        for p, s in cars:
            time = (target - p) / s
            if time > cur_time:
                ans += 1
                cur_time = time
        return ans