class Solution:
    def calculate(self, s: str) -> int:
        '''
        Use a stack, append when seeing '(', numbers, and symbols, pop when seeing ')'.
        Note that when scanning through all characters, we need to handle numbers with
        multiple digits.
        To let above logic cover equations without '()', we add '()' to wrap the input equation.
        '''
        stack = []
        num = ""
        for c in '(' + s + ')':
            if c.isdigit():
                num += c
            elif c in '()+-':
                if num:
                    stack.append(int(num))
                    num = ""
                if c in '(+-':
                    stack.append(c)
                elif c == ')':
                    res = 0
                    while stack:
                        n = stack.pop()
                        s = stack.pop()
                        if s == '+':
                            res += n
                        elif s == '-':
                            res -= n
                        elif s == '(':
                            res += n
                            break
                    stack.append(res)
        return stack[0]