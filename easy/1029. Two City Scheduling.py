class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        '''
        A person either goes to A or B, so we can sort the costs by the savings
        by going to A instead of B. We send the first N persons to A with the greatest
        N savings, and the other half must go to B.
        '''
        costs.sort(key=lambda c: c[0] - c[1])
        half = len(costs) // 2
        return sum(c[0] for c in costs[:half]) + sum(c[1] for c in costs[half:])