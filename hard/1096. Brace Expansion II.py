# 1096. Brace Expansion II
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        '''
        Stack.
        

        Similar to 772. Basic Calculator III
        '''
        stack = []
        p1 = [] # previous list with things before the last ','
        c1 = [] # current list where things are growing.
        for e in expression:
            if e.isalpha():
                c1 = [c + e for c in c1 or ['']]
            elif e == '{':
                stack.append((p1, c1))
                p1 = []
                c1 = []
            elif e == ',':
                p1 += c1
                c1 = []
            elif e == '}':
                p0, c0 = stack.pop()
                c1 = [p + c for c in p1 + c1 for p in c0 or ['']]
                p1 = p0
        return sorted(set(p1 + c1))