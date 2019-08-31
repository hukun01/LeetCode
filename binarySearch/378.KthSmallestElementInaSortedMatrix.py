class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """ 1/2 Heap method. Remember the heapq stuffs in Py. 
        The heap approach is like merge sorted arrays.
        IMPORTANT: in the tuple we store in the heap, value needs to come first, aka, use (priority, task) tuples
        Time complexity is O(k * log n), space complexity is O(n)
        
        # Init a heap with the first row
        heap = [(val, 0, j) for j, val in enumerate(matrix[0])]
        heapq.heapify(heap)
        answer = 0
        for _ in range(k):
            answer, i, j = heapq.heappop(heap)
            if i + 1 < len(matrix):
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
        return answer
        """
        """ 2/2 Another instance for binary searching the *value* spaces.
            Time complexity is O(n * log(max - min)), space complexity is O(1)
        """
        def countSmaller(upperBound):
            count, j = 0, len(matrix[0]) - 1
            # each time j moves to left or down, so the runtime would be (row + col), aka, O(n)
            for i in range(len(matrix)):
                while j >= 0 and matrix[i][j] > upperBound:
                    j -= 1
                count += j + 1
            return count
        l, h = matrix[0][0], matrix[-1][-1]
        while l < h:
            m = l + (h - l) // 2
            if countSmaller(m) < k:
                l = m + 1
            else:
                h = m
        return l