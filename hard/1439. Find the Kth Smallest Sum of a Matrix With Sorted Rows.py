# 1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        '''
        Merge K sorted list.
        
        Similar to 373. Find K Pairs with Smallest Sums.
        From #373 we pick the k smallest pair sums from two lists, based on
        that, we can use the same solution with a bit modification to return
        the k smallest pair sums instead of pairs. Then for each row in mat,
        we run this method to get the k smallest pair sums iteratively and pick
        the last one as the answer.

        Time: O(R (k log(min(k, C)))) where kSmallestPairs() takes O(k log(C)) time.
        Space: O(max(k, C))
        '''
        R, C = len(mat), len(mat[0])
        ans = mat[0]
        for i in range(1, R):
            ans = self.kSmallestPairs(ans, mat[i], k)
        return ans[-1]

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = [(a + nums2[0], a, 1) for i, a in enumerate(nums1[:min(len(nums1), k)])]
        heapify(pq)
        ans = []
        while len(ans) < k and pq:
            cur_sum, a1, i2 = heappop(pq)
            # The only difference between this and the original #373 solution.
            ans.append(cur_sum)
            if i2 < len(nums2):
                heappush(pq, (a1 + nums2[i2], a1, i2 + 1))
        return ans