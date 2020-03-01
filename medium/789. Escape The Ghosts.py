# 789. Escape The Ghosts
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        '''
        Just need to know whether it's possible, no need to find the actual path.
        Manhattan distance is enough for checking the possibility.
        '''
        def distanceToTarget(r1, c1):
            return abs(r1 - target[0]) + abs(c1 - target[1])
        toTarget = distanceToTarget(0, 0)
        for r1, c1 in ghosts:
            if distanceToTarget(r1, c1) <= toTarget:
                return False
        return True