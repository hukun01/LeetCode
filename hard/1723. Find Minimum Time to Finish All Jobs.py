# 1723. Find Minimum Time to Finish All Jobs
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        '''
        Binary search + DFS.
        

        The DFS optimization technique is similar to
        698. Partition to K Equal Sum Subsets.
        '''
        l = max(jobs)
        h = sum(jobs)
        jobs.sort(reverse=True)

        def dfs(job_idx, workers, limit):
            if job_idx == len(jobs):
                return True
            for i in range(k):
                if workers[i] >= jobs[job_idx]:
                    workers[i] -= jobs[job_idx]
                    if dfs(job_idx + 1, workers, limit):
                        return True
                    workers[i] += jobs[job_idx]

                if workers[i] == limit:
                    break
            return False

        while l < h:
            m = (l + h) // 2
            if dfs(0, [m] * k, m):
                h = m
            else:
                l = m + 1

        return h