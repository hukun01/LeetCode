# 789. Escape The Ghosts
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        '''
        The shortest path to target is Manhattan distance, if there's any
        ghost that can reach target no later than the player, the player can't
        escape.
        '''
        def distanceToTarget(point):
            return abs(point[0] - target[0]) + abs(point[1] - target[1])
        toTarget = distanceToTarget([0, 0])
        return not any(distanceToTarget(g) <= toTarget for g in ghosts)