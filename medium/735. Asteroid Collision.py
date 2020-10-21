# 735. Asteroid Collision
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        Stack.
        '''
        ans = []
        for a in asteroids:
            destroyed_a = False
            while not destroyed_a and ans and a < 0 < ans[-1]:
                if ans[-1] < abs(a):
                    ans.pop()
                    continue
                elif ans[-1] == abs(a):
                    ans.pop()
                destroyed_a = True
            if not destroyed_a:
                ans.append(a)
        return ans