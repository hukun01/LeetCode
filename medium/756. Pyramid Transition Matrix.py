# 756. Pyramid Transition Matrix
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        '''
        1/2 List out all the possible next levels, and DFS on each one.
        '''
        graph = collections.defaultdict(list)
        for a, b, c in allowed:
            graph[(a, b)].append(c)
        
        def dfs(level):
            if len(level) == 1:
                return True

            bs = [""]
            for a, b in zip(level, level[1:]):
                newB = []
                for c in graph[(a, b)]:
                    for b in bs:
                        newB.append(b + c)
                bs = newB
            return any(dfs(b) for b in bs)
        return dfs(bottom)

        '''
        2/2 Another flavor of DFS that focus on current line and the above line.
        '''
        graph = collections.defaultdict(list)
        for a, b, c in allowed:
            graph[(a, b)].append(c)
        
        def dfs2(line, start, above):
            if len(line) == 1:
                return True
            if start == len(line) - 1:
                return dfs2(above, 0, "")
            a, b = line[start], line[start + 1]
            for c in graph[(a, b)]:
                if dfs2(line, start + 1, above + c):
                    return True
            return False
        return dfs2(bottom, 0, "")