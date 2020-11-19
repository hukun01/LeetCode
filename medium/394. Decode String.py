# 394. Decode String
class Solution:
    def decodeString(self, s: str) -> str:
        stack = [["", 1]]
        num = ""
        for c in s:
            if c.isdigit():
                num += c
            elif c == '[':
                stack.append(["", int(num)])
                num = ""
            elif c == ']':
                subString, repeat = stack.pop()
                stack[-1][0] += subString * repeat
            else:
                stack[-1][0] += c
        
        return stack[0][0]