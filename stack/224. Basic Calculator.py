class Solution:
    def calculate(self, s: str) -> int:
        '''
        Use a stack, append when seeing '(', numbers, and symbols, pop when seeing ')'.
        Note that when scanning through all characters, we need to handle numbers with
        multiple digits.
        To let above logic cover equations without '()', we add '()' to wrap the input equation.
        '''
        stack = []
        currNum = ""
        for c in ("(" + s + ")"):
            if c == ' ':
                continue
            if c.isdigit():
                currNum += c
                continue
            if len(currNum) > 0:
                stack.append(int(currNum))
                currNum = ""
            if c != ')':
                stack.append(c)
                continue
            pos = neg = 0
            prevC = None
            while prevC != '(':
                prevNum = stack.pop()
                prevC = stack.pop()
                if prevC in '(+':
                    pos += prevNum
                else:
                    neg += prevNum
            stack.append(pos - neg)
                
        return stack[0]