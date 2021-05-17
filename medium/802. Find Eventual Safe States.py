# 802. Find Eventual Safe States
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
        Topological sorting.
        Starting from safe nodes where there's no outdegree, 
        reversely traverse back and find its previous nodes
        that only connect to safe nodes, and those previous
        nodes are safe too.

        Similar to 210. Course Schedule II.
        '''
        succ_count = defaultdict(int)
        pre = defaultdict(list)
        for node, succs in enumerate(graph):
            for s in succs:
                succ_count[node] += 1
                pre[s].append(node)

        safe = set(range(len(graph))) - set(succ_count)
        ans = []
        while safe:
            a = safe.pop()
            ans.append(a)
            for p in pre[a]:
                succ_count[p] -= 1
                if succ_count[p] == 0:
                    safe.add(p)
        return sorted(ans)