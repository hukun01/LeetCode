# 241. Different Ways to Add Parentheses
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        '''
        Recursion.
        For each symbol, we can add or not, a pair of parenthesis around its
        equation. If input[i] is a symbol, add the cross product of left and
        right sub-expressions: check(input[:i]) x check(input[i+1:]).

        Time: O(n^2) where n is len(input), also assuming roughly half of the
        chars are symbols that will lead to string slicing and recursion.
        Space: O(n^2), but can be simplified to O(1) by using index to replace
        string slicing.
        '''
        if input.isdigit():
            return [int(input)]
        ans = []
        for i, c in enumerate(input):
            if c not in '+-*':
                continue
            lefts = self.diffWaysToCompute(input[:i])
            rights = self.diffWaysToCompute(input[i+1:])
            for l in lefts:
                for r in rights:
                    if c == '+':
                        ans.append(l + r)
                    elif c == '-':
                        ans.append(l - r)
                    else:
                        ans.append(l * r)
        return ans