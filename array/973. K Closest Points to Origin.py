class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        '''
        1/2 Use quick select
        '''
        # The search space within the array is changing for each round - but the list,
        # is still the same size. Thus, k does not need to be updated with each round.
        def sort(start, end):
            if start >= end:
                return
            pivotIdx = partition(start, end)
            if pivotIdx > K:
                sort(start, pivotIdx - 1)
            elif pivotIdx < K:
                sort(pivotIdx + 1, end)

        dist = lambda i: points[i][0] ** 2 + points[i][1] ** 2
        # partition on a random pivotIdx such that 
        # points[start] <= points[pivotIdx] <= points[end], and start < pivotIdx < end
        def partition(start, end):
            pivotIdx = random.randint(start, end)
            pivot = dist(pivotIdx)
            points[end], points[pivotIdx] = points[pivotIdx], points[end]
            storedIdx = start
            for i in range(start, end): # excluding end
                if dist(i) < pivot:
                    points[storedIdx], points[i] = points[i], points[storedIdx]
                    storedIdx += 1
            points[end], points[storedIdx] = points[storedIdx], points[end]
            
            return storedIdx # do NOT return pivotIdx!

        sort(0, len(points) - 1)
        return points[:K]
        '''
        2/2 Use Heap

        dist = lambda i: points[i][0] ** 2 + points[i][1] ** 2
        ans = []
        for i, point in enumerate(points):
            heapq.heappush(ans, (-dist(i), point))
            if len(ans) > K:
                heapq.heappop(ans)
        return [a[1] for a in ans]
        '''