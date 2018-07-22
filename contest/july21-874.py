class Solution:
    def robotSim(self, commands, obstacles):
        """
        Store the obstacles as a tuple set, and use 2 arrays to control the direction moves.

        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        # current position
        p = [0, 0]
        dx = [0, 1, 0, -1] # N, E, S, W
        dy = [1, 0, -1, 0] # N, E, S, W
        di = 0 # index 
        obSet = set(map(tuple, obstacles))
        result = 0

        for c in commands:
            if c == -1:
                di += 1
            elif c == -2:
                di -= 1
            else:
                di = di % 4
                for i in range(c):
                    if (p[0] + dx[di], p[1] + dy[di]) not in obSet:
                        p[0] += dx[di]
                        p[1] += dy[di]
                        result = max(result, p[0]*p[0] + p[1]*p[1])
        return result