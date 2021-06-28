# 489. Robot Room Cleaner
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        '''
        DFS with backtrack.

        Three keys:
        1. The 'compass' moving directions need to be aligned with the turns.
            Robot initially face up, so we need to start with 0.
            If we keep turning left, we need to go to (-1, 0) the next;
            if we keep turning right, we need to go to (1, 0) the next.
        2. We need to go through all 4 directions, from the current direction,
            instead of from the beginning of the compass. Hence, the key here
            is to iterate 4 times, and wrap up the compass if needed. And in
            the DFS we need to propagate the current direction in dfs.
        3. Only when the potential new position is not cleaned, and robot can
            move, we will further dfs. With checking this, we will be doing
            extra backtrack, because the robot didn't actually move before.
        '''
        compass = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        def dfs(node, currDir, cleaned):
            robot.clean()
            cleaned.add(node)

            for _ in range(4):
                dr, dc = compass[currDir]
                newNode = (node[0] + dr, node[1] + dc)
                if newNode not in cleaned and robot.move():
                    dfs(newNode, currDir, cleaned)
                robot.turnLeft()
                currDir = (currDir+1) % 4

            # Go back one step, and remain the current direction
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()

        dfs((0, 0), 0, set())