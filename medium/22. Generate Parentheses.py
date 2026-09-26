class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        '''
        Keep track of the number of '(' and ')', and we can add more '('
        as long as we don't exceed the n limit, but we can only add more
        ')' when there's enough '(' in the path.

        We need to pop out the last symbol after each dfs() to build the
        other permutations.
        '''
        ans = []
        path = []
        def dfs(left, right):
            if left == right == n:
                ans.append(''.join(path))
                return
            if left < n:
                path.append('(')
                dfs(left + 1, right)
                path.pop()
            if right < left:
                path.append(')')
                dfs(left, right + 1)
                path.pop()
        
        dfs(0, 0)
        return ans
