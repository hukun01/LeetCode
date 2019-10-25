class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        '''
        Moving '0' around with BFS.
        Since the graph is so small, we can hard-code the possible steps to make search faster.
        Using 2-end BFS and 1-end is similar, because the search space is small.
        '''
        compass = { 0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4], 4: [1, 3, 5], 5: [2, 4] }
        target = "123450"
        queue = collections.deque([''.join(str(c) for row in board for c in row)])
        visited = set()
        visited.add(queue[0])
        steps = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == target:
                    return steps
                pos = node.index("0")
                for d in compass[pos]:
                    newNode = list(node)
                    newNode[d], newNode[pos] = newNode[pos], newNode[d]
                    newNode = ''.join(newNode)
                    if newNode in visited:
                        continue
                    visited.add(newNode)
                    queue.append(newNode)
            steps += 1
                    
        return -1