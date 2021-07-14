# 358. Rearrange String k Distance Apart
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        '''
        1/3 Sort + Buckets.
        Get the char count maps, sorted from high count to low.
        With highest count 'max_count', we have max_count buckets, (max_count-1)
        buckets are full.
        For each char with high count, if the count == max_count, the char
        gets added to each bucket.
        Otherwise, the char gets added to the *full* buckets 'count' times,
        and we keep the bucket index for adding the next char.
        Finally, concat all buckets.

        Note that if the (len(s) + (k - 1)) // k is less than the highest char
        frequency, then there's no way to reorganize.

        To ensure k distance, the KEY is to distinguish the buckets that should
        be full vs the final bucket that doesn't need to be full.
        If count == buckets, we should assign char to every bucket; Otherwise,
        only assign to the first (buckets - 1) buckets.
        '''
        freqs = sorted(Counter(s).items(), key=lambda i: i[1], reverse=True)
        buckets = freqs[0][1]
        if (buckets - 1) * k + sum(c[1] == buckets for c in freqs) > len(s):
            return ""

        ans = [[] for _ in range(buckets)]
        bucket_idx = 0
        for char, count in freqs:
            for _ in range(count):
                ans[bucket_idx].append(char)
                bucket_idx = (bucket_idx + 1) % (len(ans) - (count != buckets))

        return ''.join(chain(*ans))
        '''
        2/3 No sort + buckets.
        '''
        freq = Counter(s)
        buckets = max(freq.values())
        initial_chars = ''.join(char for char, v in freq.items() if v == buckets)
        if k * (buckets - 1) + len(initial_chars) > len(s):
            return ""

        ans = [[initial_chars] for _ in range(buckets)]
        bucket_idx = 0
        for char, count in freq.items():
            if count == buckets:
                continue
            for _ in range(count):
                ans[bucket_idx].append(char)
                bucket_idx = (bucket_idx + 1) % (buckets - 1)

        return ''.join(chain(*ans))
        '''
        3/3 Heap.
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