class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        1/2
        Similar to #279, BFS is faster than regular DP.
        """
        """
        if amount == 0:
            return 0
        queue = collections.deque([0])
        visited = set()
        level = 1
        while queue:
            for _ in range(len(queue)):
                curAmount = queue.popleft()
                for coin in coins:
                    newAmount = curAmount + coin
                    if newAmount == amount:
                        return level
                    if newAmount < amount and newAmount not in visited:
                        visited.add(newAmount)
                        queue.append(newAmount)
            level += 1
        return -1
        """
        """
        2/2 Regular DP: State transition: 
        nums[i] = 1 + min(nums[i - c1], nums[i - c2], ..., nums[i - c_n]), where c in coins
        and nums[0] = 0
        """
        nums = [0] + [float('inf')] * amount
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    nums[a] = min(nums[a], nums[a - c] + 1)
        return nums[-1] if nums[-1] != float('inf') else -1
        '''
        Improvement for the for loop in 2/2 above:

        for c in coins:
            for a in range(c, amount + 1):
                nums[a] = min(nums[a], nums[a - c] + 1)
        '''