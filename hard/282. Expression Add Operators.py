# 282. Expression Add Operators
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        '''
        DFS with backtrack.

        The key is to handle multiplication.
        The backtrack here is special, as we don't backtrack the expression,
        but its value. For example, given num as '1234', if we try '1+2' and
        val is 3, now if we add a '*' between 2 and 3, we have '1+2*3', now we
        lost the value of the previous 2, so we subtract it from the val, and
        add 2*3 to val.

        Time: O(4^n) where n is len(num). Let T(n) be the total valid
              expressions, if we use the first digit, we have 3*T(n-1) exp;
              if we use the first 2 digits, we have 3*T(n-2) exp. Hence
              T(n)   = 3T(n-1) + 3T(n-2) + ... + 3T(0)
              T(n-1) = 3T(n-2) + 3T(n-3) + ... + 3T(0)
              T(n-2) = 3T(n-3) + 3T(n-4) + ... + 3T(0)
              ...
              Add the second formula to the first, we have
              T(n)  = 3 * 4 * (T(n-2) + ... + T(0))
              Add the third formula to above, we have
              T(n)  = 3 * 4^2 * (T(n-3) + ... + T(0))
              This generalize to T(n) = 3 * 4^k * (T(n-k-1) ... T(0))
              if k = n - 1, we have T(n) = 3 * 4^(n-1) * T(0) = 4^n
        Space: O(n)
        '''
        ans = []
        n = len(num)
        def dfs(start = 0, path = '', val = 0, prev = None):
            if start == n and val == target:
                ans.append(path)
            for i in range(start + 1, n + 1):
                if i == start + 1 or num[start] != '0':
                    exp = num[start: i]
                    cur = int(exp)
                    if prev is None:
                        dfs(i, exp, cur, cur)
                    else:
                        dfs(i, f'{path}+{exp}', val + cur, cur)
                        dfs(i, f'{path}-{exp}', val - cur, -cur)
                        dfs(i, f'{path}*{exp}', val - prev + prev * cur, prev * cur)
        dfs()
        return ans