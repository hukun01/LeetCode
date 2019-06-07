class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        
        1/2
        BFS, each node is a number, starting from 0, an edge exists to a newNode
        if there is a node + a square number == newNode.
        Time for BFS is |V| + |E|, in this case, there are  N vertices, the number of 
        edges is tricky, but to estimate, since the edge space is sparse, we can 
        use N as well, so overall, the time is O(N).
        This is faster than regular DP, which is O(sqrt(N)*N))
        """
        """
        queue = collections.deque([0])
        visited = set()
        level = 1
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                j = 1
                while cur + j * j <= n:
                    newNum = cur + j * j
                    if newNum == n:
                        return level
                    if newNum not in visited:
                        queue.append(newNum)
                        visited.add(newNum)
                    j += 1
            level += 1
        raise ValueError("No solution found.")
        """
        """ 
        2/2 Regular DP: State transition: 
        nums[i] = 1 + min(nums[i - 1], nums[i - 4], ..., nums[i - j*j]),
        where j * j <= i
        """
        nums = [i for i in range(n + 1)]
        for i in range(1, n + 1):
            j = 1
            while j*j <= i:
                nums[i] = min(nums[i], nums[i - j*j] + 1)
                j += 1
        return nums[-1]