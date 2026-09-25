class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        '''
        Initialize a heap using each number from nums1 and the first number from nums2.
        Without this initialization, if we just add (total, 0, 0), then we have to add
        (i, j+1) and (i+1,0) each time, then we will be adding (i+1, 0) from every (i, j),
        then we will have to use a set to dedup, which is not ideal.
        '''
        ans = []
        choices = [(a + nums2[0], i, 0) for i, a in enumerate(nums1)]
        heapify(choices)
        while len(ans) < k and choices:
            _, i1, i2 = heappop(choices)
            ans.append([nums1[i1], nums2[i2]])
            if i2 + 1 == len(nums2):
                continue
            heappush(choices, (nums1[i1] + nums2[i2 + 1], i1, i2 + 1))

        return ans
