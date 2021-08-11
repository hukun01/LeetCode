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
        (max_f - 1) such periods, where max_f is the max frequency of the
        tasks. Note that there can be multiple tasks with the same
        max frequency, imagine they get combined into one task (X)
        with length being max_f_key_num, where max_f_key_num is the number of
        the most frequent tasks. In addition to filling the period,
        max_f_key_num also gets lined up at the end, so the total length would
        be (max_f - 1) * (n + 1) + max_f_key_num
        '''
        freqs = list(Counter(tasks).values())
        max_f = max(freqs)
        max_f_key_num = sum(c == max_f for c in freqs)

        return max(len(tasks), (max_f - 1) * (n + 1) + max_f_key_num)