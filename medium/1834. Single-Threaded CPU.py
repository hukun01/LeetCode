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
        available_tasks = []
        while tasks_by_e or available_tasks:
            if not available_tasks:
                time = max(time, tasks_by_e[0][0])
            while tasks_by_e and tasks_by_e[0][0] <= time:
                _, processing, task_idx = heappop(tasks_by_e)
                heappush(available_tasks, (processing, task_idx))

            processing, task_idx = heappop(available_tasks)
            ans.append(task_idx)
            time += processing

        return ans