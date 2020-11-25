# 1665. Minimum Initial Energy to Finish Tasks
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        '''
        Greedy.
        At task 't', we need 'm' energy to start it, 'a' energy to finish it, so
        we save (saved := m - a) energy after 't'.
        At the next task 't2', we need ('m2' - prev_saved) energy to start, a2 to finish.
        We need sum(a) at the minimum, the goal is to minimize the extra energy
        for starting. To do that, we want to maximize 'prev_saved' as soon as possible
        when going through the tasks.
        Hence, we sort the tasks by 'saved', reversely.
        Time: O(nlogn) where n is the length of tasks array.
        Space: O(n) for sorting.
        '''
        tasks.sort(key=lambda t: (t[1] - t[0], t[1]), reverse = True)
        ans = prev_saved = 0
        for a, m in tasks:
            if prev_saved < m:
                ans += m - prev_saved
                prev_saved = m
            prev_saved -= a
        return ans