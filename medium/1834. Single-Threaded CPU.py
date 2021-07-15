# 1834. Single-Threaded CPU
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        '''
        Greedy + heap.

        Time: O(n log(n))
        Space: O(n)
        '''
        tasks_by_e = [(enqueue, processing, i)
            for i, (enqueue, processing) in enumerate(tasks)]
        heapify(tasks_by_e)
        ans = []
        time = 1
        available = []
        while tasks_by_e or available:
            if not available:
                time = max(time, tasks_by_e[0][0])
            while tasks_by_e and tasks_by_e[0][0] <= time:
                _, processing, i = heappop(tasks_by_e)
                heappush(available, (processing, i))
            
            processing, i = heappop(available)
            ans.append(i)
            time += processing

        return ans