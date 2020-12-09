# 358. Rearrange String k Distance Apart
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        '''
        1/2 Buckets.
        Get the char count maps, sorted from high count to low.
        With highest count 'max_count', we have max_count buckets, (max_count-1)
        buckets are full.
        For each char with high count, if the count == max_count, the char
        gets added to each bucket.
        Otherwise, the char gets added to the *full* buckets 'count' times,
        and we keep the bucket index for adding the next char.
        Finally, concat all buckets.

        Note that if the (total length + (k - 1)) // k is less than the
        highest char frequency, then there's no way to reorganize.
        '''
        freqs = sorted([[c, b] for b, c in Counter(s).items()], reverse=True)
        max_count = freqs[0][0]
        if (max_count - 1) * k + sum(c[0] == max_count for c in freqs) > len(s):
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
        '''
        2/2 Heap.
        Use a heap to store all the (count, char) tuples from S.
        In every block we can only use one char once, so we always
        use the top k most common chars first.
        We do this for every block until all chars are used.
        '''
        if k == 0:
            return s
        freqs = Counter(s)
        pq = [[-count, bar] for bar, count in freqs.items()]
        heapify(pq)
        ans = []
        while pq:
            need = []
            for _ in range(k):
                if not pq:
                    if need:
                        return ""
                    continue
                count, bar = heappop(pq)
                if count + 1 != 0:
                    need.append([count + 1, bar])
                ans.append(bar)
            for entry in need:
                heappush(pq, entry)
        return ''.join(ans)