class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        '''
        For each symbol, we can add or not, a pair of parenthesis around its equation
        If input[i] is a symbol:
            check(input[:i]) x check(input[i+1:])
        
        x is to get the combination between two lists based on the symbol
        '''
        def check(start, end):
            if input[start: end].isdigit():
                return [int(input[start: end])]
            result = []
            for i in range(start, end):
                c = input[i]
                if c not in '+-*':
                    continue
                leftResult = check(start, i)
                rightResult = check(i + 1, end)
                if c == '-':
                    calc = lambda l, r: l - r
                elif c == '+':
                    calc = lambda l, r: l + r
                elif c == '*':
                    calc = lambda l, r: l * r
                else:
                    raise KeyError(f"unknown symbol {c}")
                for l in leftResult:
                    for r in rightResult:
                        result.append(calc(l, r))
            return result
        return check(0, len(input))