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
        # partition on a random m such that points[i] <= points[m] <= points[j], and i < m < j
        def partition(i, j):
            m = random.randint(i, j)
            points[j], points[m] = points[m], points[j]
            pivot = dist(j)
            storedIdx = i
            for i in range(i, j): # excluding j
                if dist(i) < pivot:
                    points[storedIdx], points[i] = points[i], points[storedIdx]
                    storedIdx += 1
            points[j], points[storedIdx] = points[storedIdx], points[j]
            
            return storedIdx # do NOT return m!

        sort(0, len(points) - 1, K)
        return points[:K]