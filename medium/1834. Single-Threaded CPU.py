# 1834. Single-Threaded CPU
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        '''
        Greedy + heap.

        Time: O(n log(n))
        Space: O(n)
        '''
        tasks_by_e = [(e, p, i) for i, (e, p) in enumerate(tasks)]
        heapify(tasks_by_e)
        ans = []
        cur_time = 1
        available_tasks = []
        while tasks_by_e or available_tasks:
            while tasks_by_e and cur_time >= tasks_by_e[0][0]:
                _, p, i = heappop(tasks_by_e)
                heappush(available_tasks, (p, i))
            if available_tasks:
                p, i = heappop(available_tasks)
                ans.append(i)
                cur_time += p
            else:
                cur_time = tasks_by_e[0][0]

        return ans