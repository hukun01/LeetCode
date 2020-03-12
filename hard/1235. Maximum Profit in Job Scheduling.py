# 1235. Maximum Profit in Job Scheduling
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        '''
        The general idea is to get the max profit from previous job schedules, and
        build the current schedule based on the previous compatible schedules.
        
        Sort the jobs by start time, (NOT end time).
        
        Iterate through the jobs, use a heap to maintain all the job schedules,
        which are represented by (end, lastProfit) entries.
        At each iteration, pop out all the job schedules that are compatible with the
        current job, and keep the 'currMax' updated to the max lastProfit we can achieve
        from all schedules.
        At the end of each iteration, we add the current job and its "profit + currMax"
        as our current schedule.
        
        A key is that, as we process the current job, 'currMax' will keep track of the
        max profit from the past schedules that are compatible with the current job.
        
        We end the iteration with a list of schedules that are mutually incompatible,
        and we find the best profit out of them.
        '''
        # represents the max profit from all compatible schedules so far.
        currMax = 0
        schedule = []
        jobs = [(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        for s, e, p in sorted(jobs):
            while schedule and schedule[0][0] <= s:
                _, lastProfit = heapq.heappop(schedule)
                currMax = max(currMax, lastProfit)
            heapq.heappush(schedule, (e, p + currMax))

        return max(j[1] for j in schedule)