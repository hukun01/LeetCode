class Solution:
    def calculate(self, s: str) -> int:
        '''
        Use a stack, append when seeing '(', numbers, and symbols, pop when seeing ')'.
        Note that when scanning through all characters, we need to handle numbers with
        multiple digits.
        To let above logic cover equations without '()', we add '()' to wrap the input equation.
        '''
        s = "(" + s.replace(' ', '') + ")"
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                numStart = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                stack.append(int(s[numStart: i]))
                continue
            elif s[i] in '+-(':
                stack.append(s[i])
            else: # s[i] == ')'
                pos = neg = 0
                prevC = None
                while prevC != '(':
                    num = stack.pop()
                    prevC = stack.pop()
                    if prevC in '(+':
                        pos += num
                    else:
                        neg += num
                stack.append(pos - neg)
            i += 1
        return stack[0]