class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        '''
        1/3 Use quick select version1
        '''
        def quickSelect(ps, k):
            pivot = ps[0]
            lefts = [p for p in ps if p < pivot]
            mids = [p for p in ps if p == pivot]
            rights = [p for p in ps if p > pivot]
            if len(lefts) < k <= len(lefts) + len(mids):
                return (lefts + mids)[:k]
            if k <= len(lefts):
                return quickSelect(lefts, k)
            return lefts + mids + quickSelect(rights, k - len(lefts) - len(mids))

        # 'ps' is the points with distance info
        ps = [(x * x + y * y, x, y) for x, y in points]
        return [[x, y] for _, x, y in quickSelect(ps, K)]
        '''
        2/3 Quick select version2
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
        '''
        3/3 Use Heap

        dist = lambda i: points[i][0] ** 2 + points[i][1] ** 2
        ans = []
        for i, point in enumerate(points):
            heapq.heappush(ans, (-dist(i), point))
            if len(ans) > K:
                heapq.heappop(ans)
        return [a[1] for a in ans]
        '''