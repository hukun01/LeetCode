# 1705. Maximum Number of Eaten Apples
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        '''
        Priority queue.
        The main idea is to eat the apple that's going to expire soon, rather
        than the apples that can remain fresh for a longer time.
        Use a priority queue to keep entries [expire_time, remaining_apples] as
        sorted, and take the earliest expiring apples first.

        Time: O(maxExpiryDay * log(maxExpiryDay))
        Space: O(n)
        '''
        n = len(apples)
        eat = 0
        heap = [] # (expire_time, remaining_apples)
        i = 0
        while heap or i < n:
            if i < n and apples[i] > 0:
                heappush(heap, [i + days[i] - 1, apples[i]])
            while heap and (heap[0][0] < i or heap[0][1] == 0):
                heappop(heap)
            if heap:
                eat += 1
                heap[0][1] -= 1
            i += 1
        return eat