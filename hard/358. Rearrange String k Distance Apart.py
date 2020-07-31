# 358. Rearrange String k Distance Apart
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        '''
        Heap.
        Use a heap to store all the (count, char) tuples from S.
        In every block we can only use one char once, so we always
        use the top k most common chars first.
        We do this for every block until all chars are used.

        Note that if the (total length + (k - 1)) // k is less than the
        highest char frequency, then there's no way to reorganize.
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