# 1847. Closest Room
from sortedcontainers import SortedList
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        '''
        Sort.

        The key is to recognize the relation between rooms and queries - we
        only use rooms whose sizes >= current query's min_size. Hence, we sort
        both rooms and queries by size info, reversely. For each query from
        small to large size requirement, we add feasible rooms to another list
        which is sorted by room index. Then we bisect in the feasible rooms
        indices.

        The idea behind processing different elements per their relative order
        is the same as 1697. Checking Existence of Edge Length Limited Paths.

        Time: O(R log(R) + Q log(Q) + Q log(R)) where R is len(rooms), Q is
              len(queries)
        Space: O(R + Q)
        '''
        reversed_sorted_rooms = sorted((size, idx) for idx, size in rooms)[::-1]

        k = len(queries)
        ans = [-1] * k
        reversed_sorted_queries = sorted((m, p, j) for j, (p, m) in enumerate(queries))[::-1]
        feasible_room_idxs = SortedList()

        r_i = 0
        for min_size, prefered_idx, j in reversed_sorted_queries:
            while r_i < len(reversed_sorted_rooms) and reversed_sorted_rooms[r_i][0] >= min_size:
                _, idx = reversed_sorted_rooms[r_i]
                feasible_room_idxs.add(idx)
                r_i += 1

            idx = feasible_room_idxs.bisect_right(prefered_idx)
            candidates = []
            if idx > 0:
                candidates.append(feasible_room_idxs[idx-1])
            if idx < len(feasible_room_idxs):
                candidates.append(feasible_room_idxs[idx])

            ans[j] = min(candidates, key=lambda x: abs(prefered_idx - x), default=-1)

        return ans