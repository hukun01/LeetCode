# 1054. Distant Barcodes
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        '''
        Heap.
        Similar to 767. Reorganize String.
        '''
        freqs = sorted([[c, b] for b, c in Counter(barcodes).items()], reverse=True)
        max_count = freqs[0][0]
        buckets = [[] for _ in range(max_count)]
        i = 0
        for c, b in freqs:
            if c == max_count:
                for bucket in buckets:
                    bucket.append(b)
            else:
                for _ in range(c):
                    buckets[i].append(b)
                    i = (i + 1) % (max_count - 1)
        return list(itertools.chain(*buckets))