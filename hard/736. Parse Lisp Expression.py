# 736. Parse Lisp Expression
class Solution:
    def evaluate(self, expression: str) -> int:
        '''
        Recursion.

        Several key points:
        1. Tokenize the expression before processing it, this simplifies the
        process logic a lot, as we don't need to check left and right parens
        or parse operators and operands, etc.
        2. Track variables within their own scope, to avoid copying var
        dictionary into every recursion.
        3. Use the tokens deque external to dfs(), this way we don't need to
        update progress BEFORE calling each dfs().

        Time: O(n) where n is len(expression)
        Space: O(n)
        '''
        tokens = deque(expression.replace('(', ' ( ').replace(')', ' ) ').split())
        variables = defaultdict(list)
        def dfs():
            x = tokens.popleft()
            if x != '(':
                if x in variables:
                    return int(variables[x][-1])
                return int(x)

            stack = []
            op = tokens.popleft()
            if op == 'let':
                while tokens:
                    # This is the last token, such as '(let x 2 sub_exp)' where
                    # sub_exp starts with '('; or '(let x 2 var)', where
                    # there's no sub_exp, but tokens[1] == ')'.
                    if tokens[0] == '(' or tokens[1] == ')':
                        val = dfs()
                        tokens.popleft() # remove ending ')'
                        while stack: # remove local scoped vars
                            variables[stack.pop()].pop()
                        return val

                    var = tokens.popleft()
                    val = dfs()
                    stack.append(var)
                    variables[var].append(val)
            else:
                if op == 'add':
                    ans = dfs() + dfs()
                else:
                    ans = dfs() * dfs()
                tokens.popleft() # remove ending ')'
                return ans

        return dfs()