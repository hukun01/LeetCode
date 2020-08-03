# 755. Pour Water
from heapq import heappop, heappush
from typing import List
class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        '''
        Heap.

        Use heaps to avoid repeated scan of the left and right parts.
        Use two heaps to store left and right heights, to find the lowest heights for every droplet.
        
        In the left heap [:K], use (height, -idx), for the same height, we need the biggest idx.
        In the right heap [K:], use (height, idx), for the same height, we need the smallest idx.
        
        After each droplet, we likely need to update the left and right heaps, because there
        can be high walls that we were not able to pass, but we are now, with more water.

        After each droplet, we also need to push the new height back.
        '''
        '''
        def debug():
            wall = max(H) + 2
            arr = [wall] + H + [wall]
            start = arr[0]
            for _ in range(arr[0]):
                print(''.join('#' if a >= start else ' ' for a in arr))
                start -= 1
        '''
        H = heights
        left = []
        left_idx = K - 1
        right = [(H[K], K)]
        right_idx = K + 1
        for _ in range(V):
            #debug()
            while left_idx >= 0 and H[left_idx] <= H[left_idx + 1]:
                heappush(left, (H[left_idx], -left_idx))
                left_idx -= 1
            while right_idx < len(H) and H[right_idx] <= H[right_idx - 1]:
                heappush(right, (H[right_idx], right_idx))
                right_idx += 1
            if left and left[0][0] < H[K]:
                height, i = heappop(left)
                H[-i] += 1
                heappush(left, (height + 1, i))
            else:
                height, i = heappop(right)
                H[i] += 1
                heappush(right, (height + 1, i))
        return H