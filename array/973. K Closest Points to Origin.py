class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = lambda i: points[i][0] ** 2 + points[i][1] ** 2
        # partially sort A[i:j + 1] so that the first K elements are less than the right part
        def sort(i, j, K):
            if i >= j:
                return
            m = partition(i, j)
            if K < m - i + 1: # K is an absolute number, while m is an index
                sort(i, m - 1, K)
            elif K > m - i + 1:
                sort(m + 1, j, K - (m - i + 1))
            
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
            
            return storedIdx
                
        sort(0, len(points) - 1, K)
        return points[:K]