class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
        Poping the tail of each string, and add it to the answer c.
        At the end, reverse the answer string.
        '''
        c = []
        carry = 0
        a = list(a)
        b = list(b)
        while a or b:
            char_a = int(a.pop()) if a else 0
            char_b = int(b.pop()) if b else 0
            add = char_a + char_b + carry
            char_c = str(add % 2)
            carry = add // 2
            c.append(char_c)
        if carry:
            c.append(str(carry))
        return ''.join(reversed(c))
