# 347. Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        1/2 Word count and a heap. The heap is to store the top k (freq, word),
        but not in the right order, because heap is min-heap, so the freq is reversely ordered,
        but the word is correctly ordered. But we keep the heap size at most k, and sort
        the heap with O(klogk) time.
        '''
        ans = []
        for n, f in Counter(nums).items():
            if len(ans) == k:
                heappushpop(ans, (f, n))
            else:
                heappush(ans, (f, n))
        return [p[1] for p in ans]

        '''
        2/2 Bucket sort the frequency-num array, and pick the first k.

        Space is O(n) for the buckets, time is O(n) for counting + picking the
        first k nums in the buckets.
        '''
        freqs = [[] for _ in nums]
        for num, freq in Counter(nums).items():
            freqs[-freq].append(num)
        return list(itertools.chain(*freqs))[:k]