class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        The key is to have concise logic. 

        Note that we don't need to keep validating BOTH nums1 and nums2's indices, 
        because if nums2 is exhausted, then the rest of nums1 is already sorted; 
        if nums1 is exhausted, then we just need to copy the rest of nums2 into the free space in nums1.
        
        Also, the major index that we use to populate nums1 would be updated when we update m or n.
        """
        while m > 0 and n > 0:
            idx = m + n - 1
            if nums1[m - 1] > nums2[n - 1]:
                nums1[idx] = nums1[m - 1]
                m -= 1
            else:
                nums1[idx] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]