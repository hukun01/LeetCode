# 947. Most Stones Removed with Same Row or Column
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        '''
        Union find.
        We can't remove the last stone in a connected component.
        For each connected component with n_c nodes, we can do
        (n_c - 1) moves. So the total move is sum(n_c - 1 for all c),
        which is sum(n_c) - c, and c is the number of connected components.
        '''
        uf = {}
        def find(point):
            if uf[point] != point:
                uf[point] = find(uf[point])
            return uf[point]
            
        for r, c in stones:
            rPoint = ('r', r)
            cPoint = ('c', c)
            uf.setdefault(rPoint, rPoint)
            uf.setdefault(cPoint, cPoint)
            uf[find(rPoint)] = find(cPoint)
        
        return len(stones) - len(set(find(p) for p in uf))