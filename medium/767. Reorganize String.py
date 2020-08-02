# 767. Reorganize String
class Solution:
    def reorganizeString(self, S: str) -> str:
        '''
        Buckets.
        Similar to 358. Rearrange String k Distance Apart.
        '''
        k = 2
        freqs = sorted([[c, b] for b, c in Counter(S).items()], reverse=True)
        max_count = freqs[0][0]
        if (max_count - 1) * k + sum(max_count == c[0] for c in freqs) > len(S):
            return ""

        buckets = [[] for _ in range(max_count)]
        i = 0
        for count, char in freqs:
            if count == max_count:
                for bucket in buckets:
                    bucket.append(char)
            else:
                for _ in range(count):
                    buckets[i].append(char)
                    i = (i + 1) % (max_count - 1)

        return ''.join(itertools.chain(*buckets))