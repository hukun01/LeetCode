# 1094. Car Pooling
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        Array.
        Same as 370. Range Addition.
        '''
        people = [0] * 1001
        for p, s, e in trips:
            people[s] += p
            people[e] -= p
        for i in range(1, len(people)):
            people[i] += people[i-1]
        return max(people) <= capacity