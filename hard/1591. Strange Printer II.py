class Solution:
    def isPrintable(self, A: List[List[int]]) -> bool:
        '''
        1/2 Finding cycle in the graph.
        The key is to build the dependencies between colors.
        A color C's next color can be found by:
            Find the max boundaries of C, and in that rectangle, all
            other colors are the next colors of color C.
        Once we build the dependency graph, the next step is to check for
        cycles. A O(C^2) time DFS is easy, where C is the number of colors.
        We can also use topological sorting to check for cycles, but it
        doesn't help much on the runtime because C is small.
        '''
        R, C = len(A), len(A[0])
        # top, left, bottom, right edge for each color
        edges = [[R, C, 0, 0] for _ in range(61)]
        colors = set()
        for r in range(R):
            for c in range(C):
                color = A[r][c]
                colors.add(color)
                edges[color][0] = min(edges[color][0], r)
                edges[color][1] = min(edges[color][1], c)
                edges[color][2] = max(edges[color][2], r)
                edges[color][3] = max(edges[color][3], c)

        nexts = defaultdict(set)
        for color in colors:
            for r in range(edges[color][0], edges[color][2]+1):
                for c in range(edges[color][1], edges[color][3]+1):
                    if A[r][c] != color:
                        nexts[color].add(A[r][c])
        visited = set()
        def hasCycle(color):
            for nex in nexts[color]:
                if nex in visited:
                    return True
                visited.add(nex)
                if hasCycle(nex):
                    return True
                visited.remove(nex)
            return False

        return not any(hasCycle(color) for color in colors)
        '''
        2/2 Greedy.
        Collects the edges for all colors, and try erase them one by one.
        When erasing a color C, ensure all colors in its boundary are either
        erased or the same as C.
        If all colors can be erased, it's printable.
        '''
        R, C = len(A), len(A[0])
        # top, left, bottom, right edge for each color
        edges = [[R, C, 0, 0] for _ in range(61)]
        colors = set()
        for r in range(R):
            for c in range(C):
                color = A[r][c]
                colors.add(color)
                edges[color][0] = min(edges[color][0], r)
                edges[color][1] = min(edges[color][1], c)
                edges[color][2] = max(edges[color][2], r)
                edges[color][3] = max(edges[color][3], c)
        
        def erase(color):
            for r in range(edges[color][0], edges[color][2] + 1):
                for c in range(edges[color][1], edges[color][3] + 1):
                    if A[r][c] > 0 and A[r][c] != color:
                        return False
            for r in range(edges[color][0], edges[color][2] + 1):
                for c in range(edges[color][1], edges[color][3] + 1):
                    A[r][c] = 0
            return True
        
        while colors:
            colors2 = set()
            for c in colors:
                if not erase(c):
                    colors2.add(c)
            if len(colors2) == len(colors):
                return False
            colors = colors2
        return True