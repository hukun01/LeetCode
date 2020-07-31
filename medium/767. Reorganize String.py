# 767. Reorganize String
class Solution:
    def reorganizeString(self, S: str) -> str:
        '''
        Heap.
        Similar to 358. Rearrange String k Distance Apart.
        '''
        k = 2
        freqs = Counter(S)
        pq = [(-count, char) for char, count in freqs.items()]
        heapify(pq)
        if -pq[0][0] > (len(S) + (k - 1)) // k:
            return ""
        ans = []
        while pq:
            counts = []
            for _ in range(k):
                if not pq:
                    break
                count, char = heappop(pq)
                if count + 1 != 0:
                    counts.append((count + 1, char))
                ans.append(char)
            for count, char in counts:
                heappush(pq, (count, char))
        return ''.join(ans)