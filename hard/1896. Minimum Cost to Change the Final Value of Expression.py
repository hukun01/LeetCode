# 1896. Minimum Cost to Change the Final Value of Expression
class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        '''
        Stack.

        Each 0 or 1 is an expression, things inside the (nested) parenthesis
        pair are independent expressions that can be calculated separately.

        Use a stack to store the last expression, each entry is [dp0, dp1, op],
        where dp0 is the number of steps to make the expression evaluates to 0,
        dp1 is that to make 1, and op is the operator, either & or |.

        When we see 'e' being 0 or 1, dp0 = int(e != '0'), dp1 = int(e != '1').
        When we see an expression with &,
            to make it 0, we need to make either dp0 or dp1 0;
            to make it 1, we need to make both dp0 and dp1 1, or make one of
            them 1, and update & to |.
        Similar logic applies to expressions with |.
        A single 0 or 1 is also considered an expression.

        Time: O(n) where n is len(expression)
        Space: O(n)

        Similar to 224. Basic Calculator.
        '''
        stack = [[0, 0, None]]
        for e in expression:
            if e == '(':
                stack.append([0, 0, None]) 
            elif e in ')01':
                if e == ")":
                    dp0, dp1, _ = stack.pop()
                else:
                    dp0, dp1 = int(e != '0'), int(e != '1')

                prev_dp0, prev_dp1, _ = stack[-1]
                if stack[-1][2] == '&':
                    stack[-1] = [
                        min(prev_dp0, dp0),
                        min(prev_dp1 + dp1, min(prev_dp1, dp1) + 1),
                        None
                    ]
                elif stack[-1][2] == '|':
                    stack[-1] = [
                        min(prev_dp0 + dp0, min(prev_dp0, dp0) + 1),
                        min(prev_dp1, dp1),
                        None
                    ]
                else:
                    stack[-1] = [dp0, dp1, None]
            elif e in '&|':
                stack[-1][2] = e
        return max(stack[0][0], stack[0][1]) 