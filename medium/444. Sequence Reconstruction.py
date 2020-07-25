# 444. Sequence Reconstruction
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        '''
        1/2 Topological sort.
        '''
        succ = defaultdict(list)
        indegree = defaultdict(int)
        nodes = set()
        for seq in seqs:
            nodes |= set(seq)
            indegree[seq[0]] += 0
            for c1, c2 in zip(seq, seq[1:]):
                succ[c1].append(c2)
                indegree[c2] += 1
        free = [k for k in indegree if indegree[k] == 0]
        res = []
        while len(free) == 1:
            cur = free.pop()
            res.append(cur)
            for nex in succ[cur]:
                indegree[nex] -= 1
                if indegree[nex] == 0:
                    free.append(nex)

        return len(free) <= 1 and len(res) == len(nodes) and res == org
        '''
        2/2 
        '''
        START = -math.inf
        def get_pairs(seq):
            prev = START
            for val in seq:
                yield prev, val
                prev = val
        ranks = {x: i for i, x in enumerate(org)}
        ranks[START] = -1
        orders = set(get_pairs(org))
        for seq in seqs:
            for x, y in get_pairs(seq):
                if x not in ranks or y not in ranks or ranks[x] >= ranks[y]:
                    return False
                orders.discard((x, y))
        return len(orders) == 0