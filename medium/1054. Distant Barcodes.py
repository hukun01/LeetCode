# 1054. Distant Barcodes
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        '''
        Sort + assign to buckets.
        Similar to 767. Reorganize String.
        '''
        freqs = sorted(Counter(barcodes).items(), key=lambda i: i[1], reverse=True)
        buckets = freqs[0][1]
        ans = [[] for _ in range(buckets)]
        bucket_idx = 0
        for num, count in freqs:
            for _ in range(count):
                ans[bucket_idx].append(num)
                bucket_idx = (bucket_idx + 1) % len(ans)
        return list(chain(*ans))