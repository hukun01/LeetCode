# 692. Top K Frequent Words
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        Heap.
        The tricky part is to return the smallest word when there are more
        than one words that share frequency. We want to sort the words 
        in increasing order, and sort the frequencies in decreasing order.
        Thus, we flip the sign of frequencies, and sort increasingly.

        heapq.nsmallest(k) has O(nlogk) time, where n is the number of unique
        words, and it returns the values in order.
        '''
        freqs = [(c, w) for w, c in Counter(words).items()]
        keyfunc = lambda p: (-p[0], p[1])
        return [w for c, w in nsmallest(k, freqs, key=keyfunc)]