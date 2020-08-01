# 621. Task Scheduler
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        Math.
        There are two cases, one is that the most frequent tasks
        are not frequent enough to create idle slots with given n;
        Another case is they are frequent to create idle slots.
        
        In the first case, the answer is just the length of tasks.

        In the second case, each period's size is (n + 1), and there are
        (f_max - 1) such periods, where f_max is the max frequency of the
        tasks. Note that there can be multiple tasks with the same
        max frequency, imagine they get combined into one task (X)
        with length being n_max, where n_max is the number of the
        most frequent tasks. In addition to filling the period, n_max
        also gets lined up at the end, so the total length would be
        (f_max - 1) * (n + 1) + n_max
        '''
        freq = list(Counter(tasks).values())
        f_max = max(freq)
        n_max = sum(c == f_max for c in freq)
        
        return max(len(tasks), (f_max - 1) * (n + 1) + n_max)