# 1054. Distant Barcodes
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        '''
        Heap.
        Similar to 767. Reorganize String.
        '''
        pq = [[-count, bar] for bar, count in Counter(barcodes).items()]
        heapify(pq)
        ans = []
        k = 2
        while pq:
            need = []
            for _ in range(k):
                if not pq:
                    break
                count, bar = heappop(pq)
                if count + 1 != 0:
                    need.append([count + 1, bar])
                ans.append(bar)
            for entry in need:
                heappush(pq, entry)
        return ans