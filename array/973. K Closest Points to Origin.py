class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        dist = lambda i: points[i][0] ** 2 + points[i][1] ** 2
        # partially sort A[i:j + 1] so that the first K elements are less than the right part
        def sort(i, j, K):
            if i >= j:
                return
            m = partition(i, j)
            if K < m - i + 1:
                sort(i, m - 1, K)
            elif K > m - i + 1:
                sort(m + 1, j, K - (m - i + 1))
            
        # return a random m such that points[i] <= points[m] <= points[j], and i <= m <= j
        def partition(i, j):
            m = random.randint(i, j)
            points[i], points[m] = points[m], points[i]
            pivot = dist(i)
            oi = i
            i += 1
            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j:
                    break
                points[i], points[j] = points[j], points[i]
            
            points[oi], points[j] = points[j], points[oi]
            return j
                
        sort(0, len(points) - 1, K)
        return points[:K]