# 378. Kth Smallest Element in a Sorted Matrix
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        '''
        1/2 Heap.
        The heap approach is like merge sorted arrays.
        Use a heap to keep the n smallest elements.
        The initial n smallest are the first row. We also track each element's
        position (r, c).
        The current element in the heap will be the smallest.
        We then keep adding the smallest element's next element (r+1, c), which
        will be the next element for the current n elements sequence.

        Note that in the tuple we store in the heap, value comes first,
        aka, use (priority, task) tuples.
        Time: O(k * log n),
        Space complexity is O(n)
        '''
        # Init a heap with the first row
        heap = []
        b = matrix
        n = len(b)
        for c in range(n):
            heapq.heappush(heap, (b[0][c], 0, c))
        ans = 0
        for _ in range(k):
            ans, r, c = heapq.heappop(heap)
            if r + 1 < n:
                heapq.heappush(heap, (b[r + 1][c], r + 1, c))
        return ans
        '''
        2/2 Another instance for binary searching the *value* spaces.
        Time: O(n * log(max - min))
        Space: O(1)
        '''
        def countSmaller(upperBound):
            count, j = 0, len(matrix[0]) - 1
            # each time j moves to left or down, so the runtime would be (row + col), aka, O(n)
            for row in matrix:
                while j >= 0 and row[j] > upperBound:
                    j -= 1
                count += j + 1
            return count
        l, h = matrix[0][0], matrix[-1][-1]
        while l < h:
            m = (l + h) // 2
            if countSmaller(m) < k:
                l = m + 1
            else:
                h = m
        return l