class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        1/3
        Similar to #279, BFS is faster than regular DP.
        '''
        q = deque([amount])
        coins.sort()
        visited = set()
        steps = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node in visited:
                    continue
                visited.add(node)
                if node == 0:
                    return steps
                for c in coins:
                    if c > node:
                        break
                    q.append(node - c)

            steps += 1

        return -1
        '''
        2/3 DP.
        Let f[i] be the min number of coins to make up amount 'i'. We have
        f[i] = 1 + min(f[i - c1], f[i - c2], ..., f[i - c_n]), where c <= i.
        f[0] = 0

        Time: O(n)
        Space: O(n)
        '''
        f = [0] + [inf] * amount
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    f[a] = min(f[a], f[a - c] + 1)
        return f[-1] if f[-1] != inf else -1
        '''
        Improvement for the for loop in 2/2 above:

        for c in coins:
            for a in range(c, amount + 1):
                f[a] = min(f[a], f[a - c] + 1)
        '''
        '''
        3/3 DFS with pruning.
        This is fast because we are able to quickly find solution for cases
        with huge amount and relative small coin value.
        For example, amount = 10000, coins = [1,2,3,4,5,6,100]. In DP we need
        O(amount * len(coins)) time, while in DFS, we quickly find self.ans to
        be 10000/100 = 100, and later we can prune most of the search branches
        based on the current answer, largely reduce the time.

        This degrades to be as fast as DP, when all the coins don't share gcd
        with any amount, e.g., when all coins are primes.
        '''
        def dfs(count, cur_amount, coin_i):
            if coin_i == len(coins):
                return

            coin = coins[coin_i]
            need = amount - cur_amount

            if need % coin == 0:
                self.ans = min(self.ans, count + need // coin)

            if count + need // coin >= self.ans:
                return

            for j in range(need // coin, -1, -1):
                dfs(count + j, cur_amount + coin * j, coin_i + 1)

        self.ans = inf
        coins.sort(reverse = True)
        dfs(0, 0, 0)
        return -1 if self.ans == inf else self.ans