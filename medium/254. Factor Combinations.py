# 254. Factor Combinations
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        '''
        DFS with backtrack.
        Keep dividing the last element in the path, using i from [2, sqrt(n)].
        We don't take numbers beyond sqrt(n) because that will lead to
        duplicate results. E.g., n = 6, we only need [2, 3], but not [3, 2].

        Also, e.g., n = 12, we have [12] -> [2, 6] -> [2, 2, 3], and [12] ->
        [3, 4] -> [3, 2, 2], the last one is a duplicate. To avoid that, we
        need to pass in the 'start' of the divisor to the DFS.

        Time: Not sure, something around sqrt(n)
        Space: Not sure.
        '''
        ans = []
        def dfs(path, start):
            num = path.pop()
            while start * start <= num:
                if num % start == 0:
                    nex = num // start
                    ans.append(path + [start, nex])
                    dfs(path + [start, nex], start)
                start += 1

        dfs([n], 2)
        return ans