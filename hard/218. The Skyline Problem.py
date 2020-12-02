# 218. The Skyline Problem
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        '''
        Sort + Priority queue.
        For each building, it has two intervals, one is [left, height, right],
        another is [right, 0, inf]. We need the second one to tell when the
        building is out of scope, and to record the key point on the bottom
        right of the last building. We sort this interval list, so we can scan
        through it from left to right. Note that we make the height to negative
        so the max ones come first when the left boundaries are the same.

        As we scan through the building intervals, use a heap to record the
        current max height and its boundary. If the heap boundary is outside
        of or on the current building interval's left boundary, we keep poping
        the current max height out. If there's a non-0 height from the
        interval, it's a new building coming into the scope, we add it to the
        heap. Whenever the latest skyline key point has different height than
        the current max height, we add the new key point using current max.
        Note that we initialize the heap with (0, inf), meaning 0 height always
        exists.

        Time: O(n log(n)) where n is len(buildings). This comes from sorting
              the interval list. Same time is taken on scanning through the
              intervals, and do at most n heap push and pop, respectively,
              each of which takes O(log(n)).
        Space: O(n)
        '''
        boundaries = []
        for l, r, h in buildings:
            boundaries.append((l, -h, r))
            boundaries.append((r, 0, inf))

        boundaries.sort()
        heights_boundary = [(0, inf)] # (height, ending_boundary)
        skyline = []
        for start, neg_h, end in boundaries:
            while heights_boundary[0][1] <= start:
                heappop(heights_boundary)
            if neg_h != 0:
                heappush(heights_boundary, (neg_h, end))
            cur_max_height = -heights_boundary[0][0]
            if not skyline or skyline[-1][1] != cur_max_height:
                skyline.append([start, cur_max_height])
        return skyline