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
        direction = 0
        visited = set()
        compass = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def turnTo(targetDir):
            nonlocal direction
            while direction != targetDir:
                direction = (direction+1) % 4
                robot.turnRight()
        cleaned = set()
        def dfs(node):
            robot.clean()
            cleaned.add(node)
            for d in compass:
                newNode = (node[0] + d[0], node[1] + d[1])
                if newNode in visited or newNode in cleaned:
                    continue
                if d[1] == 1:
                    # go up
                    turnTo(0)
                elif d[1] == -1:
                    # go down
                    turnTo(2)
                elif d[0] == 1:
                    # go right
                    turnTo(1)
                elif d[0] == -1:
                    # go left
                    turnTo(3)
                if not robot.move():
                    continue
                visited.add(newNode)
                dfs(newNode)
                visited.remove(newNode)
                
                if d[1] == 1:
                    # go down
                    turnTo(2)
                elif d[1] == -1:
                    # go up
                    turnTo(0)
                elif d[0] == 1:
                    # go left
                    turnTo(3)
                elif d[0] == -1:
                    # go right
                    turnTo(1)
                robot.move()
        visited.add((0, 0))
        dfs((0, 0))