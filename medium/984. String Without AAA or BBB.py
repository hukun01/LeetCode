# 984. String Without AAA or BBB
class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        '''
        Buckets.
        Similar to 358. Rearrange String k Distance Apart.
        '''
        (first, x), (second, y) = sorted([(A, 'a'), (B, 'b')], reverse=True)
        buckets = [x + x] * (first // 2)
        if first % 2 == 1:
            buckets.append(x)
        num_buckets = len(buckets)
        bucket_idx = 0
        for _ in range(second):
            buckets[bucket_idx % num_buckets] += y
            bucket_idx += 1
        return ''.join(buckets[:min(num_buckets, bucket_idx + 1)])