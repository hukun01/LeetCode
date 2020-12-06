# 605. Can Place Flowers
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        '''
        Greedy.
        There is no benefit in skipping a good slot, so we greedily take each
        one. A good slot is an empty one whose left and right are also empty.

        Time: O(F) where F is len(flowerbed)
        Space: O(1)
        '''
        F = len(flowerbed)
        for i in range(F):
            left_good = i - 1 < 0 or flowerbed[i - 1] == 0
            right_good = i + 1 == F or flowerbed[i+1] == 0
            if left_good and right_good and flowerbed[i] == 0:
                n -= 1
                flowerbed[i] = 1
            if n <= 0:
                break
        return n <= 0