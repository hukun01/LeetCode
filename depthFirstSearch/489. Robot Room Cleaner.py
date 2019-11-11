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
        The 'compass' moving directions need to be aligned with the turns.
        No matter which direction the robot is facing, we need to go through all 4 directions.
        Only when the potential new position is not cleaned, and robot can move, we will further dfs.

        Robot initially face up, so we need to start with (0, 1).
        If we keep turning left, we need to go to (-1, 0) the next;
        if we keep turning right, we need to go to (1, 0) the next.
        '''
        compass = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        def dfs(node, currDir, cleaned):
            robot.clean()
            cleaned.add(node)
            
            for _ in range(4):
                d = compass[currDir]
                newNode = (node[0] + d[0], node[1] + d[1])
                if newNode not in cleaned and robot.move():
                    dfs(newNode, currDir, cleaned)
                robot.turnLeft()
                currDir = (currDir+1) % 4
            
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
                
        dfs((0, 0), 0, set())