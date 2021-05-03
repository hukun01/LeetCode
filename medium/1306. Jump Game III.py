# 1306. Jump Game III
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        '''
        Graph traversal.

        Regular DFS with 'visited' set.
        Any graph traversal can solve this.

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