class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        '''
        1/2 Quick select version2
        Similar to 215. Kth Largest Element in an Array
        The search space within the array is changing for each round - but the list,
        is still the same size. Thus, k does not need to be updated with each round.
        '''
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

        start = 0
        end = len(points) - 1

        while start <= end:
            pivotIdx = partition(start, end)
            if pivotIdx > K:
                end = pivotIdx - 1
            elif pivotIdx < K:
                start = pivotIdx + 1
            else:
                break
        return points[:K]
        '''
        2/2 Heap
        '''
        return heapq.nsmallest(K, points, key=lambda p: (p[0] ** 2 + p[1] ** 2) ** 0.5)