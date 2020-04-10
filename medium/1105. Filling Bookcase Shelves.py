# 1105. Filling Bookcase Shelves
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        '''
        Let f[i] be the min total height to arrange books[:i], aka, the first i-1 books.
        
        State transitions:
        f[0] = 0
        f[i] = min(f[i], f[j] + max(heights[j:i]) for all j such that sum(width[j:i][0]) <= shelf_width)
        '''
        n = len(books)
        f = [math.inf] * (n + 1)
        f[0] = 0
        for i in range(1, n + 1):
            height = totalWidth = 0
            for j in range(i-1, -1, -1):
                if totalWidth + books[j][0] > shelf_width:
                    break
                totalWidth += books[j][0]
                height = max(height, books[j][1])
                f[i] = min(f[i], f[j] + height)
        return f[-1]