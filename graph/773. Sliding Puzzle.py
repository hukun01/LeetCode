class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        '''
        Moving '0' around with BFS.
        Since the graph is so small, we can hard-code the possible steps to make search faster.
        Using 2-end BFS and 1-end is similar, because the search space is small.
        '''
        ends = set(["123450"])
        starts = set([''.join([str(cell) for row in board for cell in row])])
        visited = set()
        compass = {0: {1, 3}, 1: {0, 2, 4}, 2: {1, 5}, 3: {0, 4}, 4: {1, 3, 5}, 5: {2, 4}}
        steps = 0
        while len(starts) > 0 and len(ends) > 0:
            if len(starts) > len(ends):
                starts, ends = ends, starts
            newStarts = set()
            for node in starts:
                if node in ends:
                    return steps
                if node in visited:
                    continue
                visited.add(node)
                oldI = node.index("0")
                for newI in compass[oldI]:
                    nodeList = list(node)
                    nodeList[oldI], nodeList[newI] = nodeList[newI], nodeList[oldI]
                    newNode = ''.join(nodeList)
                    newStarts.add(newNode)
            starts = newStarts
            steps += 1
        return -1