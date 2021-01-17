# 767. Reorganize String
class Solution:
    def reorganizeString(self, S: str) -> str:
        '''
        Sort + assign to buckets.
        Similar to 358. Rearrange String k Distance Apart.
        '''
        freqs = sorted(Counter(S).items(), key=lambda i: i[1], reverse=True)
        buckets = freqs[0][1]
        if buckets > len(S) - buckets + 1:
            return ""
        ans = [[] for _ in range(buckets)]
        bucket_idx = 0
        for num, count in freqs:
            for _ in range(count):
                ans[bucket_idx].append(num)
                bucket_idx = (bucket_idx + 1) % len(ans)
        return ''.join(chain(*ans))