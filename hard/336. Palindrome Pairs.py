# 336. Palindrome Pairs
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        '''
        A straightforward way is to try all possible strings,
        say we have n words, then we need to try n^2 times.
        Each time, we iterate through the whole string, say average word length
        is k, then the total time would be (n^2) * k. This would be too slow.
        
        Use P to denote palindrome
        There are 4 cases in which words form a P
        1. w2 is P, w1 is empty, then w1 + w2 is a P, and w2 + w1 is a P;
        2. w2 is the reversed w1, then w1 + w2 is a P
        3. w1[0:x] is a P, w2 is the reversed w1[x:], then w2 + w1 is a P. This covers case 2 when x is 0.
        4. w1[x:] is a P, w2 is the reversed w1[0:x], then w1 + w2 is a P. This covers case 1 when x is len(w1).
        '''
        def is_palin(w):
            return w == w[::-1]
        word_to_idx = { w: i for i, w in enumerate(words) }
        ans = []

        # 1/2 A shorter translation of the last 2 cases above with extented coverages.
        for w, i in word_to_idx.items():
            for cut in range(len(w) + 1):
                left = w[:cut]
                right = w[cut:]
                if is_palin(left) and (right_reversed := right[::-1]) in word_to_idx:
                    # case 2 and 3
                    if (j := word_to_idx[right_reversed]) != i:
                        ans.append([j, i])
                # We already checked the case (left == "", right == w), no need to check
                # the case (left == w, right == "").
                if cut != len(w) and is_palin(right) and (left_reversed := left[::-1]) in word_to_idx:
                    # case 1 and 4
                    ans.append([i, word_to_idx[left_reversed]])
        return ans

        '''
        2/2 A more straightforward translation of the 4 cases above.
        '''
        # case 1
        if "" in word_to_idx:
            a = word_to_idx[""]
            for b, w in enumerate(words):
                if is_palin(w) and a != b:
                    ans.append([a, b])
                    ans.append([b, a])
        # case 2
        for a, w in enumerate(words):
            r = w[::-1]
            if r in word_to_idx:
                b = word_to_idx[r]
                if a != b:
                    ans.append([a, b])
        # case 3 and 4
        for a, w in enumerate(words):
            for x in range(1, len(w)):
                left = w[:x]
                right = w[x:]
                right_reversed = right[::-1]
                if is_palin(left) and right_reversed in word_to_idx:
                    ans.append([word_to_idx[right_reversed], a])
                left_reversed = left[::-1]
                if is_palin(right_reversed) and left_reversed in word_to_idx:
                    ans.append([a, word_to_idx[left_reversed]])
        return ans