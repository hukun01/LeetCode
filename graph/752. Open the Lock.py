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
        start = "0000"
        begin = set([start])
        end = set([target])
        steps = 0
        while begin and end:
            if len(begin) > len(end):
                x = begin
                begin = end
                end = x
            
            temp = set()
            for s in begin:
                if s in end:
                    return steps
                if s in deads:
                    continue
                deads.add(s)
                for i in range(4):
                    s1 = updateString(s, i, int(s[i]) + 1)
                    s2 = updateString(s, i, int(s[i]) - 1)
                    temp.add(s1)
                    temp.add(s2)
            steps += 1
            begin = temp
            
        return -1