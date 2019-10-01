class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        '''
        Solve 2D problem based on 1D case. In 1D array, we just find the median,
        and sum the distance from each element to the median.
        2D is just 1D(all rows) + 1D(all cols).
        To solve for 1D, it's possible without median, we just count the number of people
        on each side. Assuming 'left' and 'right' are the number of people
        before left index l and after right index r, then left = sum(nums[:l+1]), 
        right = sum(nums[r:]). And say 'd' is the total distance for left people to meet
        at 'l', and for right people to meet at 'r'.
        Our goal is to let l == r, with minimum d.
        If we increase l by 1, d will increase by left; if we decrease r by 1, d will increase
        by right. To achieve a minimum d, we move the min(left, right) in every iteration.
        '''
        def minTotalDistance1D(nums):
            l, r = -1, len(nums)
            d = left = right = 0
            while l < r:
                if left < right:
                    d += left
                    l += 1
                    left += nums[l]
                else:
                    d += right
                    r -= 1
                    right += nums[r]
            return d
        
        rowSums = list(map(sum, grid))
        colSums = list(map(sum, zip(*grid)))
        
        return minTotalDistance1D(rowSums) + minTotalDistance1D(colSums)