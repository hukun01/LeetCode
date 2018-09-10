class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool

        This is still a sliding window stuff, but specifically with buckets.
        Use buckets with dict to collect the nearby values, remember to use (t + 1) in case t == 0.
        """
        if k < 0 or t < 0: # we are asked for absolute diff, so t < 0 wouldn't work.
            return False
        
        bucket = {}
        w = t + 1
        for i, num in enumerate(nums):
            bucketId = num // w

            for nearBy in (bucketId - 1, bucketId, bucketId + 1):
                if nearBy in bucket and abs(bucket[nearBy] - num) <= t:
                    return True

            # We don't need to store multiple values in a bucket.
            # Because if that is a case, we should return True above.
            # We always update the bucket with the latest (right most) value.
            bucket[bucketId] = num

            if i >= k:
                expired = nums[i - k] // w
                bucket.pop(expired)

        return False