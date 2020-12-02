# 1029. Two City Scheduling
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        '''
        Sort by savings.
        A person either goes to A or B, so we can sort the costs by the savings
        by going to A instead of B. We send the first N persons to A with the
        greatest N savings, and the other half must go to B.

        Time: O(n log(n))
        Space: O(sort) which is O(n) in Python
        '''
        costs.sort(key=lambda c: c[0] - c[1])
        n = len(costs) // 2
        return sum(c[0] for c in costs[:n]) + sum(c[1] for c in costs[n:])