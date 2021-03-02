# 1776. Car Fleet II
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        '''
        Mono stack.

        The current car speed would not be affected by its left cars, but only
        be affected by its right slower cars. Hence, we visit cars from right
        to left. Use a stack to track the car index whose collision time is
        strictly decreasing (cars closer to stack top collide earlier).

        Assume cars a,b,c on the road, if 'a' collide on 'b' LATER than 'b'
        collide on 'c', then 'a' collide on 'b+c', instead of colliding on 'b'.
        In this case, imagine the 'b' disappear after colliding, and the stack
        top will track the position of 'c' - the actual first car 'a' collides.

        Time: O(n)
        Space: O(n)
        '''
        n = len(cars)
        ans = [inf] * n
        stack = []
        for i in range(n-1, -1, -1):
            pos, speed = cars[i]
            while stack:
                last = stack[-1]
                last_pos, last_speed = cars[last]
                if speed > last_speed and (last_pos - pos) / (speed - last_speed) < ans[last]:
                    break
                else:
                    stack.pop()

            if stack:
                last_pos, last_speed = cars[stack[-1]]
                ans[i] = (last_pos - pos) / (speed - last_speed)

            stack.append(i)

        return [i if i != inf else -1 for i in ans]