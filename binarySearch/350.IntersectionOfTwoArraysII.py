class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        """ Leveraging Counter, an object works like word count, it's a dict subclass.
        a, b = map(collections.Counter, (nums1, nums2))
        return list((a & b).elements())
        """ 
        
        """Leveraging sorted attributed.
        """
        nums1.sort()
        nums2.sort()
        i1, i2 = 0, 0
        result = []
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] == nums2[i2]:
                result.append(nums1[i1])
                i1 += 1
                i2 += 1
            elif nums1[i1] > nums2[i2]:
                i2 = bisect.bisect_right(nums2, nums2[i2])
            else:
                i1 = bisect.bisect_right(nums1, nums1[i1])
        return result