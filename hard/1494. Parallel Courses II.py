# 1494. Parallel Courses II
class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        '''
        Use bitmask to represent the state of what couses had been taken.
        Use bitmask to represent the prerequisites of a course.
        Use a queue to track the (taken courses, number of semesters).
        Every iteration, explore the free courses based on taken ones and
        prereqs. For the free courses, try all different subset with size k,
        like BFS.
        '''
        prereqs = defaultdict(int)
        for pre, post in dependencies:
            prereqs[post] |= 1 << (pre - 1)
        target_mask = (1 << n) - 1
        queue = deque([(0, 0)])
        visited = {0}
        while queue:
            taken, num_semesters = queue.popleft()
            free_courses = [x for x in range(1, n + 1) if (taken & (1 << (x - 1)) == 0) and taken & prereqs[x] == prereqs[x]]
            for courses in itertools.combinations(free_courses, min(k, len(free_courses))):
                new_taken = taken
                for x in courses:
                    new_taken |= 1 << (x - 1)
                if new_taken == target_mask:
                    return num_semesters + 1
                if new_taken not in visited:
                    visited.add(new_taken)
                    queue.append((new_taken, num_semesters + 1))