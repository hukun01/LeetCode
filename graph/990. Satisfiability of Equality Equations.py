# 990. Satisfiability of Equality Equations
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        '''
        Union find.

        First handle all '==' equations to build the connected components.
        Then handle all '!=' equations to see if there is any conflict.
        '''
        uf = { a: a for a in string.ascii_letters }
        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        
        for eq in [e for e in equations if e[1] == '=']:
            uf[find(eq[0])] = find(eq[-1])
            
        for ne in [e for e in equations if e[1] == '!']:
            if find(ne[0]) == find(ne[-1]):
                return False
        return True