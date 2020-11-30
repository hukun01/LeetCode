# 1306. Jump Game III
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        '''
        DFS with cycle detection.
        Regular DFS, except that we need to check whether the current position
        has been visited before. If so, we are in a cycle and need to return.
        Time: O(n) where n is the length of the array.
        Space: O(n)
        '''
        def dfs(visited, pos):
            if not 0 <= pos < len(arr):
                return False
            if pos in visited:
                return False
            visited.add(pos)
            if (num := arr[pos]) == 0:
                return True
            return dfs(visited, pos + num) or dfs(visited, pos - num)

        return dfs(set(), start)