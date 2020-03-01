# 756. Pyramid Transition Matrix
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        '''
        1/2 List out all the possible next levels, and DFS on each one.
        '''
        graph = collections.defaultdict(list)
        for a, b, c in allowed:
            graph[(a, b)].append(c)
        
        def dfs(bottom):
            if len(bottom) == 1:
                return True
            
            pairs = []
            for i in range(len(bottom) - 1):
                a = bottom[i]
                b = bottom[i + 1]
                pairs.append((a, b))
            bs = [[]]
            for p in pairs:
                newB = []
                for c in graph[p]:
                    for b in bs:
                        newB.append(b + [c])
                bs = newB
            return any(dfs(b) for b in bs)
        return dfs(bottom)

        '''
        2/2 Another flavor of DFS that focus on current line and the above line.
        '''
        maps = collections.defaultdict(set)
        for c1, c2, c3 in allowed:
            maps[(c1, c2)].add(c3)
        
        def dfs(line, start, above):
            if len(line) == 1:
                return True
            if start == len(line) - 1:
                return dfs(above, 0, "")
            c1, c2 = line[start], line[start + 1]
            for c3 in maps[(c1, c2)]:
                if dfs(line, start + 1, above + c3):
                    return True
            return False
        return dfs(bottom, 0, "")