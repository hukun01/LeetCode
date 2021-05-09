class Solution:
    def alienOrder(self, words: List[str]) -> str:
        '''
        Topological sorting.
        Find the prerequisite pairs by iterating every 2 words, and do
        topological sorting on the pair list.
        '''
        nexts = defaultdict(list)
        indegree = {c: 0 for c in chain(*words)}
        for w1, w2 in zip(words, words[1:]):
            chars = next(((c1, c2) for c1, c2 in zip(w1, w2) if c1 != c2), None)
            if chars:
                cur, nex = chars
                indegree[nex] += 1
                nexts[cur].append(nex)
            else:
                if len(w1) > len(w2):
                    return ""

        q = deque([a for a, v in indegree.items() if v == 0])

        ans = []
        while q:
            a = q.popleft()
            ans.append(a)
            for b in nexts[a]:
                indegree[b] -= 1
                if indegree[b] == 0:
                    q.append(b)

        if len(ans) != len(indegree):
            return ""

        return ''.join(ans)