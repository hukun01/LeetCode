# 1235. Maximum Profit in Job Scheduling
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        '''
        1/2 DP.
        Let f[j] be the max profit for jobs[:j].
        f[j+1] = max(f[j], f[prev(j)] + profit[j]), this means that for the
        current job j, we have two choices:
            1. skip it, nothing change in f, f[j+1] = f[j].
            2. do it, we find the previous job in f that ends before current
               job starts, so they are compatible. Then we pick the larger
               profit between doing j vs skipping j.

        In above transition function, prev(j) defines the largest job index
        that ends before j starts.

        We sort jobs by end time, this ensures that we check jobs in
        chronological order.
        Note that we put endTime at front, to enable bisect() to work.
        Also note that we need to search for (start + 1, -inf) tuple, in order
        to locate the earliest job that ends after 'start', so the whole
        'bisect() - 1' would be the latest job that ends before or at 'start'.

        Time: O(n log(n)) for sort and DP.
        Space: O(n)
        '''
        jobs = sorted(zip(endTime, startTime, profit), key=lambda e: e[0])
        n = len(jobs)
        f = [0] * (n + 1)
        def prev(x):
            start = jobs[x][1]
            return bisect_right(jobs, (start + 1, -inf)) - 1
            '''
            # Equivalent to below linear time process:
            while x >= 0 and jobs[x][0] > start:
                x -= 1
            return x
            '''

        for j in range(n):
            f[j + 1] = max(f[j], jobs[j][2] + f[prev(j) + 1])
        return f[-1]
        '''
        1/2 Another implementation of above DP idea.
        Let f[-1] be the latest [end, max_profit_so_far]. As we iterate
        through jobs, for each job, if we can find a bigger profit, we will do
        it, so we append the new [new_end, new_max_profit]. If the current job
        and its previous compatible (job, profit) can't exceed the existing max
        profit, then we don't do it.
        '''
        jobs = sorted(zip(startTime, endTime, profit), key=lambda e: e[1])
        f = [[0, 0]]
        for s, e, p in jobs:
            i = bisect_right(f, [s + 1, -inf]) - 1
            if f[i][1] + p > f[-1][1]:
                f.append([e, f[i][1] + p])

        return f[-1][1]
        '''
        2/2 Priority queue.
        The general idea is to get the max profit from previous job schedules,
        and build the current schedule based on the previous compatible schedules.
        
        Sort the jobs by start time, (NOT end time).
        
        Iterate through the jobs, use a heap to maintain all the job schedules,
        which are represented by (end, last_profit) entries.
        At each iteration, pop out all the job schedules that are compatible
        with the current job, and keep the 'curr_max_profit' updated to the
        max last_profit we can achieve from all schedules.
        At the end of each iteration, we add the current job and its
        "profit + curr_max_profit" as our current schedule.
        
        A key is that, as we process the current job, 'curr_max_profit'
        will keep track of the max profit from the past schedules that
        are compatible with the current job.
        
        We end the iteration with a list of schedules that are mutually
        incompatible, and we find the best profit out of them.

        Time: O(n log(n)) for sort and priority queue operations.
        Space: O(n)
        '''
        # represents the max profit from all compatible schedules so far.
        curr_max_profit = 0
        schedule = []
        jobs = sorted(zip(startTime, endTime, profit))
        for s, e, p in jobs:
            while schedule and schedule[0][0] <= s:
                _, last_profit = heappop(schedule)
                curr_max_profit = max(curr_max_profit, last_profit)
            heappush(schedule, (e, p + curr_max_profit))

        return max(j[1] for j in schedule)