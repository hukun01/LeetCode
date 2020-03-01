class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        '''
        For each symbol, we can add or not, a pair of parenthesis around its equation
        If input[i] is a symbol:
            check(input[:i]) x check(input[i+1:])
        
        x is to get the combination between two lists based on the symbol
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