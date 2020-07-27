# 444. Sequence Reconstruction
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        '''
        1/2 Topological sort.
        '''
        succ = defaultdict(list)
        indegree = defaultdict(int)
        seen_in_seqs = set()
        for seq in seqs:
            seen_in_seqs.update(seq)
            for c1, c2 in zip(seq, seq[1:]):
                succ[c1].append(c2)
                indegree[c2] += 1
        if len(seen_in_seqs) != len(org):
            return False
        free = list(seen_in_seqs - set(indegree))
        res = []
        while len(free) == 1:
            cur = free.pop()
            res.append(cur)
            for nex in succ[cur]:
                indegree[nex] -= 1
                if indegree[nex] == 0:
                    free.append(nex)

        return len(free) <= 1 and res == org
        '''
        2/2 Ensure orders between every pair in ord and seqs.
        Similar to topological sort.
        '''
        START = -math.inf
        def get_pairs(seq):
            yield START, seq[0]
            for c1, c2 in zip(seq, seq[1:]):
                yield c1, c2
        ranks = {x: i for i, x in enumerate(org)}
        ranks[START] = -1
        orders = set(get_pairs(org))
        for seq in seqs:
            for x, y in get_pairs(seq):
                if x not in ranks or y not in ranks or ranks[x] >= ranks[y]:
                    return False
                orders.discard((x, y))
        return len(orders) == 0