class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        e = expression
        i = 0
        stack = []
        while i < len(e):
            if e[i] in '!&|':
                stack.append(e[i])
                i += 1
            elif e[i] == ')':
                operands = []
                while stack and not isinstance(stack[-1], str):
                    operands.append(stack.pop())
                operator = stack.pop()
                if operator == '!':
                    stack.append(not operands[0])
                if operator == '&':
                    stack.append(all(operands))
                if operator == '|':
                    stack.append(any(operands))
            elif e[i] in 'tf':
                stack.append(e[i] == 't')
            i += 1
        return stack.pop()