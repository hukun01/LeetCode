class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        '''
        When seeing a number, push into the stack;
        Otherwise, evaluate.
        Note that division truncates toward zero means when
        dividing a negative number, '//' in py will truncate toward
        the floor, which can be -1 in examples like '3//-4'.
        So we need to use 'int(a/b)' to get truncate correctly.
        '''
        stack = []
        for t in tokens:
            if t in { '+', '-', '*', '/' }:
                b = stack.pop()
                a = stack.pop()
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(t))

        return stack[0]
