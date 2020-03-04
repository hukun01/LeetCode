# 789. Escape The Ghosts
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        '''
        Just need to know whether it's possible, no need to find the actual path.
        Manhattan distance is enough for checking the possibility.
        '''
        def distanceToTarget(point):
            return abs(point[0] - target[0]) + abs(point[1] - target[1])
        toTarget = distanceToTarget([0, 0])
        return not any(distanceToTarget(g) <= toTarget for g in ghosts)