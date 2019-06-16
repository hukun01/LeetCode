class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # The search space within the array is changing for each round - but the list,
        # is still the same size. Thus, k does not need to be updated with each round.
        def sort(start, end, k):
            if start >= end:
                return
            pivotIdx = partition(start, end)
            if pivotIdx > k:
                sort(start, pivotIdx - 1, k)
            elif pivotIdx < k:
                sort(pivotIdx + 1, end, k)

        dist = lambda i: points[i][0] ** 2 + points[i][1] ** 2
        # partition on a random pivotIdx such that 
        # points[start] <= points[pivotIdx] <= points[end], and start < pivotIdx < end
        def partition(start, end):
            pivotIdx = random.randint(start, end)
            pivot = dist(pivotIdx)
            points[end], points[m] = points[m], points[end]
            storedIdx = start
            for i in range(start, end): # excluding end
                if dist(i) < pivot:
                    points[storedIdx], points[i] = points[i], points[storedIdx]
                    storedIdx += 1
            points[end], points[storedIdx] = points[storedIdx], points[end]
            
            return storedIdx # do NOT return pivotIdx!

        sort(0, len(points) - 1, K)
        return points[:K]