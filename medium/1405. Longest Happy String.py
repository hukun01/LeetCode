# 1405. Longest Happy String
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        '''
        Buckets.
        Similar to 358. Rearrange String k Distance Apart
        and 984. String Without AAA or BBB.
        '''
        (first, x), (second, y), (third, z) = sorted(
            [(a, 'a'), (b, 'b'), (c, 'c')], reverse=True)
        buckets = [x + x] * (first // 2)
        if first % 2 == 1:
            buckets.append(x)
        num_buckets = len(buckets)
        bucket_idx = 0
        for count, char in [(second, y), (third, z)]:
            for _ in range(count):
                buckets[bucket_idx % num_buckets] += char
                bucket_idx += 1
        # There may be no enough separator between each bucket, so we only
        # take the ones that are separated.
        return ''.join(buckets[:min(num_buckets, bucket_idx + 1)])