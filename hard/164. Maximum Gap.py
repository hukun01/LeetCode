# 164. Maximum Gap
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        '''
        Bucket sort.
        Usually when sort() is not an option, bucket sort is likely a way to
        organize values with the cost of some extra space.

        The intuition behind bucket sort here is that we can group values that
        are too close(to be considered contributing to the final answer) in the
        same bucket. Then the inter-bucket gap will contain the actual max gap.

        To group values we need O(n) time, to traverse buckets we need O(b)
        time where b is the number of buckets, and b is capped by n. Hence this
        is overall O(n) time, and same for space.

        Let maxi, mini be the max and min of nums, n be len(nums).
        How to decide what values to group in the same bucket? Notice that the
        min possible gap is (maxi - mini) / (n - 1), when all gaps are evenly
        distributed. We can use this as the bucket size, for 2 reasons:
            1. Any larger bucket size can mistakenly include 2 elements that
               create max gap;
            2. Any smaller bucket size is unnecessary, because even if the min
               gap is the only gap in the nums, inter-bucket gap would just be
               the same as the actual max gap.
        Note that bucket_size = max(1, (maxi - mini) / (n - 1)) to handle cases
        that may have lots of duplicate values and cause min gap to be 0.

        Knowing bucket_size, bucket_count = (maxi - mini) / bucket_size + 1.
        The extra +1 is to ensure the bucket index is correctly mapping to the
        values. E.g., the largest bucket index is (maxi - mini) / bucket_size.

        Know we can group values into buckets, how to calculate inter-bucket
        gap? Assume we have 2 buckets as below, then the gap should be
        'min_val2 - max_val1', because they are consecutive values in the
        sorted array.
        [a, b, c, min_val1, max_val1], [d, e, f, min_val2, max_val2]
        Hence, in the bucket we need to track 3 things:
            1. used flag: whether this bucket has any values;
            2. max_val: the max_val in this bucket;
            3. min_val: the min_val in this bucket;

        Time: O(n)
        Space: O(n)
        '''
        n = len(nums)
        if n < 2:
            return 0

        maxi = max(nums)
        mini = min(nums)

        bucket_size = max(1, (maxi - mini) // (n - 1))
        bucket_count = (maxi - mini) // bucket_size + 1
        buckets = [Bucket() for _ in range(bucket_count)]

        for a in nums:
            bucket_id = (a - mini) // bucket_size
            bucket = buckets[bucket_id]
            bucket.used = True
            bucket.max_val = max(a, bucket.max_val)
            bucket.min_val = min(a, bucket.min_val)

        prev_bucket_max = mini
        max_gap = 0
        for bucket in buckets:
            if not bucket.used:
                continue
            max_gap = max(max_gap, bucket.min_val - prev_bucket_max)
            prev_bucket_max = bucket.max_val

        return max_gap

class Bucket:
    def __init__(self):
        self.used = False
        self.max_val = -inf
        self.min_val = inf