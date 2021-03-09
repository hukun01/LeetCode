# 1700. Number of Students Unable to Eat Lunch
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        '''
        Word count.
        Key is to notice that we don't need to simulate the student queue.
        As long as there's ANY student in the queue that prefers the current
        sandwiches, he's going to get it, because others will skip it. Hence,
        have a Counter() to track the overall remaining students' preferences,
        and consume the sandwich until no one prefers the current sandwich.

        Time: O(n) where n is len(students)
        Space: O(1)
        '''
        student_counts = Counter(students)
        i = 0
        n = len(sandwiches)
        while i < n and student_counts[sandwiches[i]] > 0:
            student_counts[sandwiches[i]] -= 1
            i += 1
        return n - i