class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        Shortest path - BFS. There are 3 keys:
        1. To update a char in a string in python we need to create a new string, to do 
           that, we need to convert the original string into a list, and do updates to it.
        2. We need to restrict the range of the possible lock slots: [0, 9].
        3. We need to keep expanding deadendSet so we keep shrinking our search space.
        """
        def updateString(string, index, num):
            li = list(string)
            li[index] = str(num % 10)
            return ''.join(li)
        
        deads = set(deadends)
        begin = set(["0000"])
        end = set([target])
        steps = 0
        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin
            
            nextLevel = set()
            for lock in begin:
                if lock in deads:
                    continue
                if lock in end:
                    return steps
                deads.add(lock)
                for i in range(4):
                    for way in [1, -1]:
                        newLock = updateString(lock, i, int(lock[i]) + way )
                        nextLevel.add(newLock)
            steps += 1
            begin = nextLevel
            
        return -1