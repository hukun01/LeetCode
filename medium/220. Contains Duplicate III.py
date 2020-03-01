class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """
        This is a sliding window stuff, but specifically with buckets.
        Buckets are built based on values; a sliding window is built for keeping the index nearby.
        Remember to use (t + 1) as the bucket size, to handle the case: t == 0.
        """
        # we are asked for [distinct] indicies, so k <= 0 wouldn't work
        # we are asked for absolute diff, so t < 0 wouldn't work.
        if k <= 0 or t < 0:
            return False

        bucket = {}
        w = t + 1
        for i, num in enumerate(nums):
            bucketId = num // w

            # Make sure don't misuse nearBy and bucketId below
            for nearBy in (bucketId - 1, bucketId, bucketId + 1):
                if nearBy in bucket and abs(bucket[nearBy] - num) <= t:
                    return True

            # We don't need to store multiple values in a bucket.
            # Because if that is a case, we should return True above.
            # We always update the bucket with the latest (right most) value.
            bucket[bucketId] = num

            if i - k >= 0:
                expired = nums[i - k] // w
                bucket.pop(expired)

        return False