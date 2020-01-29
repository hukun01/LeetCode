# 1235. Maximum Profit in Job Scheduling
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        '''
        The general idea is to get the max profit from current job schedules, and build the next
        schedule based on the current compatible schedules.
        
        Sort the jobs by start time, (NOT end time).
        
        Iterate through the jobs, use a heap to maintain all the job schedules,
        which are represented by (end, totalProfit) entries.
        At each iteration, pop out all the job schedules that are compatible with the next
        job, and keep the 'ans' updated to the max totalProfit we can achieve from all schedules.
        At the end of each iteration, we add the job and its profit as our latest schedule.
        
        A key is that, as we process the next job, 'ans' will keep track of the max profit from
        the past schedules that are compatible with the next job, because the next job has a
        greater-or-equal start time, as we sorted the jobs that way.
        
        We end the iteration with a list of schedules that are mutually incompatible, and we find
        the best profit out of them.
        '''
        jobs = [(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        ans = 0
        heap = []
        for s, e, p in sorted(jobs):
            while heap and heap[0][0] <= s:
                _, lastProfit = heapq.heappop(heap)
                ans = max(ans, lastProfit)
            heapq.heappush(heap, (e, p + ans))
        
        while heap:
            _, lastProfit = heapq.heappop(heap)
            ans = max(ans, lastProfit)
        return ans