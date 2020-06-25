class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        '''
        1/2 Shortest path - Two-end BFS.
        Three keys:
        1. To update a char in a string in python we need to create a new string, to do 
           that, we need to convert the original string into a list, and do updates to it.
        2. Restrict the range of the possible lock slots: [0, 9].
        3. Keep expanding deadends_set so to shrink the search space.
        '''
        deadends_set = set(deadends)
        steps = 0
        begins = set(['0000'])
        ends = set([target])
        def find_next_node(node):
            for i in range(len(node)):
                for move in [-1, 1]:
                    next_node = list(node)
                    next_node[i] = str((int(next_node[i]) + move) % 10)
                    yield ''.join(next_node)
        
        while begins and ends:
            if steps % 2 == 0:
                begins, ends = ends, begins
            next_level = set()
            for node in begins:
                if node in deadends_set:
                    continue
                deadends_set.add(node)

                if node in ends:
                    return steps

                next_level.update(find_next_node(node))
            begins = next_level
            steps += 1
        return -1
        '''
        2/2 Regular BFS.
        '''
        def find_next_node(node):
            for i in range(len(node)):
                for move in [-1, 1]:
                    next_node = list(node)
                    next_node[i] = str((int(next_node[i]) + move) % 10)
                    yield ''.join(next_node)
        deadends_set = set(deadends)
        queue = deque(['0000'])
        steps = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node in deadends_set:
                    continue
                deadends_set.add(node)

                if node == target:
                    return steps

                queue += list(find_next_node(node))
            steps += 1
        return -1