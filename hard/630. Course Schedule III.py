# 630. Course Schedule III
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        '''
        Greedy + heap.
        Similar to other interval schedule problems, and also intuitively,
        we prefer the courses with earlier deadlines, so we sort them by
        deadlines. Then as we go through the courses, keep track of the current
        days, and a max heap of taken course durations.
        For each course, we always take it first. After taking it, if the
        current days exceeds the current deadline, we remove the longest
        course from the max heap. This means that we do one of below:
        1. replace the longest course with the current course, while both
           have deadlines less than or equal to the current deadline. The
           total courses count remains, and the current days decreases.
        2. add the current course initially, but remove it instantly as its
           duration is too long, the courses count and current days remains.

        During this process our 'taken' heap is monotonically incrementing.
        At the end we get a list of course durations while maintaining the fact
        that the current days doesn't exceed any deadline. Hence, the length
        of the list is the courses count we need.

        Time: O(n log(n)) where n is len(courses)
        Space: O(n)
        '''
        taken = []
        cur_day = 0
        for duration, end in sorted(courses, key=lambda c: c[1]):
            cur_day += duration
            heappush(taken, -duration)
            if cur_day > end:
                prev_duration = -heappop(taken)
                cur_day -= prev_duration

        return len(taken)