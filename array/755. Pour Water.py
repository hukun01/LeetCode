class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        '''
        1/2 Use heaps to avoid repeated scan of the left and right parts.

        Use two heaps to store left and right heights, to find the lowest heights for every droplet.
        
        In the left heap [:K], use (height, -idx), for the same height, we need the biggest idx.
        In the right heap [K:], use (height, idx), for the same height, we need the smallest idx.
        
        After each droplet, we likely need to update the left and right heaps, because there
        can be high walls that we were not able to pass, but we are now with more water.
        '''
        left = []
        right = []
        i1 = K - 1
        i2 = K + 1
        heapq.heappush(right, (heights[K], K))
        for _ in range(V):
            while i1 >= 0 and heights[i1] <= heights[i1 + 1]:
                heapq.heappush(left, (heights[i1], -i1))
                i1 -= 1
            while i2 < len(heights) and heights[i2] <= heights[i2 - 1]:
                heapq.heappush(right, (heights[i2], i2))
                i2 += 1
            if left and left[0][0] < heights[K]:
                h, idx = heapq.heappop(left)
                heights[-idx] += 1
                heapq.heappush(left, (heights[-idx], idx))
                continue
            # It must be true: right and right[0][0] < heights[K]:
            h, idx = heapq.heappop(right)
            heights[idx] += 1
            heapq.heappush(right, (heights[idx], idx))
        return heights

        '''
        2/2 Simple simulation of the droplet movement.

        Follow the droplet simulation, try left, then try right, then try to move back
        to K-th in case right side is as high as K-th.
        

        for _ in range(V):
            i = K
            # Try left
            while i > 0 and heights[i] >= heights[i - 1]:
                i -= 1

            # Try right
            while i < len(heights) - 1 and heights[i] >= heights[i + 1]:
                i += 1
            
            # In case the right is the same height, we try to move the droplet back to K-th.
            while i > K and heights[i] >= heights[i - 1]:
                i -= 1
                
            heights[i] += 1
        return heights
        '''