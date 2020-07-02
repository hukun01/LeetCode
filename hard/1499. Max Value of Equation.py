# 1499. Max Value of Equation
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        '''
        Transform the problem, we are looking for the max of below equation.
        yi + yj + xj - xi = yi - xi + xj + yj
        Hence this is similar to 239. Sliding Window Maximum, but the max
        we need is (yi - xi), and we need two elements in the window.
        '''
        q = deque()
        ans = -math.inf
        for x, y in points:
            while q and x - q[0][1] > k:
                q.popleft()
            if q:
                ans = max(ans, q[0][0] + x + y)
            while q and q[-1][0] <= y - x:
                q.pop()
            q.append((y - x, x))
        return ans