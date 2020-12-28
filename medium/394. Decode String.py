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
                sub_string, repeat = stack.pop()
                stack[-1][0] += sub_string * repeat
            else:
                stack[-1][0] += c

        return stack[0][0]