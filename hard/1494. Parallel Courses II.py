# 1494. Parallel Courses II
class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        '''
        
        '''
        graph = defaultdict(int)
        for pre, post in dependencies:
            graph[post] |= 1 << (pre - 1)
        target_mask = (1 << n) - 1
        queue = deque([(0, 0)])
        visited = {0}
        while queue:
            mask, num_semesters = queue.popleft()
            free_courses = [x for x in range(1, n + 1) if (mask & (1 << (x - 1)) == 0) and mask & graph[x] == graph[x]]
            for courses in itertools.combinations(free_courses, min(k, len(free_courses))):
                new_mask = mask
                for x in courses:
                    new_mask |= 1 << (x - 1)
                if new_mask == target_mask:
                    return num_semesters + 1
                if new_mask not in visited:
                    visited.add(new_mask)
                    queue.append((new_mask, num_semesters + 1))