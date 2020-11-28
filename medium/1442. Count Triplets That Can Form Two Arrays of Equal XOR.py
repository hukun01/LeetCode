# 1442. Count Triplets That Can Form Two Arrays of Equal XOR
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        '''
        1/2 O(N^2)
        a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
        b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k - 1]
        If a == b, we know a ^ b == 0, then
        arr[i] ^ arr[i + 1] ^ ... ^ arr[k - 1] == 0.
        
        Let preXors[i] be the prefix xor for arr[:i],
        if a == b, we have preXors[k] ^ preXors[i] == 0,
        which is preXors[k] == preXors[i].
        
        And j can be any index within (i, k-1] in arr,
        so we add (k - 1 - i) to the result.
        '''
        preXors = [0]
        for i in arr:
            preXors.append(preXors[-1] ^ i)

        ans = 0
        for i in range(len(preXors) - 1):
            for k in range(i + 1, len(preXors)):
                if preXors[k] == preXors[i]:
                    ans += k - 1 - i
        return ans
        '''
        1/2 O(N)
        Based on 1/2, we look for the size of (i, k-1] interval and the number of such intervals.
        In those intervals, preXors[k] == preXors[i].
        The answer is the sum of [size * count for all such intervals].
        Say we are at index k-1 in arr, and preXors[k] == x, and x has occured c times at k_1, ..k_c previously,
        we will add this to our answer: (k - 1 - k_1) + ... + (k - 1 - k_c) = (k - 1) * c - (k_1 + ... + k_c).
        So we maintain a frequency counter, and a total counter, for every preXors[k].
        '''
        preXors = [0]
        for i in arr:
            preXors.append(preXors[-1] ^ i)

        total = Counter()
        count = Counter()
        ans = 0
        for k, prefix in enumerate(preXors):
            ans += count[prefix] * (k - 1) - total[prefix]
            count[prefix] += 1
            total[prefix] += k
        return ans