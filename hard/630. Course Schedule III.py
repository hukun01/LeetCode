# 630. Course Schedule III
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        '''
        Greedy + heap.
        Similar to other interval schedule problems, and also intuitively,
        we prefer the courses with earlier deadlines, so we sort them using
        their deadlines. Then as we go through the courses, keep track of the
        total days, and a sorted list of taken course days.
        For each course, after taking it, if the total days exceeds the
        current deadline, we remove the longest course. This means that we
        do one of below:
        1. replace the longest course with the current course, while both
           have deadlines less than or equal to the current deadline. The
           total number of courses remain, but the total days decreases.
        2. add the current course initially, but remove it instantly as its
           days is too long.
        At the end we get a list of course days while maintaining the fact
        that the total days doesn't exceed any deadline. Hence, the length
        of the list is the number of courses we can take.

        Time: O(n log(n)) where n is len(courses)
        Space: O(n)
        '''
        taken = []
        cur_day = 0
        for t, end in sorted(courses, key=lambda c: c[1]):
            cur_day += t
            heappush(taken, -t)
            if cur_day > end:
                pre_t = -heappop(taken)
                cur_day -= pre_t

        return len(taken)