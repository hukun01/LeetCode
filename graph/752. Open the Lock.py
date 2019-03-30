class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        Shortest path - BFS. There are 3 keys:
        1. To update a char in a string in python we need to create a new string, to do 
           that, we need to convert the original string into a list, and do updates to it.
        2. We need to restrict the range of the possible lock slots: [0, 9].
        3. We need to keep expanding deadendSet so we keep shrinking our search space.
        """
        deadendSet = set(deadends)
        start = "0000"
        if start in deadendSet:
            return -1
        
        queue = collections.deque([start])
        step = 0
        def updateString(string, idx, delta):
            chars = list(string)
            val = int(chars[idx])
            val = (val + delta) % 10
            chars[idx] = str(val)
            return ''.join(chars)
        
        def foundTarget(string):
            if string == target:
                return True
            if string not in deadendSet:
                queue.append(string)
                deadendSet.add(string)
            return False
        
        while queue:
            step += 1
            for _ in range(len(queue)):
                current = queue.popleft()
                for i in range(4):
                    up = updateString(current, i, 1)
                    if foundTarget(up):
                        return step
                    down = updateString(current, i, -1)
                    if foundTarget(down):
                        return step
                        
        return -1