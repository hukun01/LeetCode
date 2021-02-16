# 1054. Distant Barcodes
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        '''
        1/2 Sort + assign to buckets.

        Time: O(n log(n)) where n is len(barcodes)
        Space: O(n)

        Similar to 767. Reorganize String.
        '''
        freqs = sorted(Counter(barcodes).items(), key=lambda i: i[1], reverse=True)
        max_count = freqs[0][1]
        buckets = [[] for _ in range(max_count)]
        bucket_idx = 0
        for num, count in freqs:
            for _ in range(count):
                buckets[bucket_idx].append(num)
                bucket_idx = (bucket_idx + 1) % len(buckets)
        return list(chain(*buckets))
        '''
        2/2 Find the most frequent and assign to buckets.

        Without sorting, only need to fill the most frequent element first,
        and fill the rest in any order. If there are multiple most frequent
        elements, fill any of them first.
        This works because no other element would never meet the same value
        when chaining the buckets, because to do that the element needs to have
        at least (n + 1) / 2 frequency, and that's impossible because it would
        have been the most frequent element.

        Time: O(n)
        Space: O(n)
        '''
        freqs = Counter(barcodes)
        most_frequent_val = max(freqs, key=lambda i: freqs[i])
        max_count = freqs[most_frequent_val]
        buckets = [[most_frequent_val] for _ in range(max_count)]
        freqs.pop(most_frequent_val)
        i = 0
        for val, count in freqs.items():
            for _ in range(count):
                buckets[i].append(val)
                i = (i + 1) % len(buckets)

        return list(chain(*buckets))