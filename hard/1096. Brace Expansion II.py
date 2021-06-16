# 1096. Brace Expansion II
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        '''
        Stack.

        We define p1 and c1, where p1 is the previous list with things before
        the last ','; c1 is the current list where things are growing.
        Each expression within '{}' is at its own level, together, p1 and c1
        form the total result at the current level.

        When we see a '{', save the current results to the stack, and restart
        the process;
        When we see a letter, expand that to the current growing list;
        When we see a comma, add the current list to the previous list, and
        start a new growing list;
        When we see a '}', combine the total result at this level with the
        previous level's growing list. This is the key. Example: in {a,b{c,d}},
        previous level would be [['a'], ['b']], p1 = ['c'], c1 = ['d'], so we
        should update to c1 = ['bc', 'bd'] by multiplying c0 and p1+c1, also
        update to p1 = ['a'].

        Here we concat strings, so it's not the fastest solution, but it can
        be easily updated to use list append.

        Time: O(n) where n is the length of the result.
        Space: O(n)

        Similar to 736. Parse Lisp Expression
        Similar to 772. Basic Calculator III
        '''
        stack = []
        p1 = []
        c1 = []
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
                c1 = [last + cur for cur in p1 + c1 for last in c0 or ['']]
                p1 = p0

        return sorted(set(p1 + c1))