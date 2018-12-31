class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        1/2
        Similar to #279, BFS is faster than regular DP.
        """
        """
        if amount == 0:
            return 0
        queue = collections.deque([0])
        visited = set([0])
        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curAmount = queue.popleft()
                for coin in coins:
                    newAmount = curAmount + coin
                    if newAmount == amount:
                        return level + 1
                    if newAmount < amount and newAmount not in visited:
                        visited.add(newAmount)
                        queue.append(newAmount)
            level += 1
        return -1
        """
        """
        2/2 Regular DP: State transition: 
        nums[i] = min(nums[i - c1] + 1, nums[i - c2] + 1, ..., nums[i - c_n] + 1),
        where c in coins
        """
        nums = [float('inf') for i in range(amount + 1)]
        nums[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if c > i:
                    continue
                nums[i] = min(nums[i], nums[i - c] + 1)
        return nums[-1] if nums[-1] != float('inf') else -1