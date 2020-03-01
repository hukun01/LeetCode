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
        def isP(w):
            return w == w[::-1]
        mappings = { w: i for i, w in enumerate(words) }
        ans = []

        # 1/2 A shorter translation of the last 2 cases above with extented coverages.
        for w, a in mappings.items():
            for cut in range(len(w) + 1):
                left = w[:cut]
                right = w[cut:]
                if isP(left):
                    rightReversed = right[::-1]
                    if rightReversed in mappings:
                        # case 2 and 3
                        if mappings[rightReversed] != a:
                            ans.append([mappings[rightReversed], a])
                # We already checked the case (left == "", right == w), no need to check
                # the case (left == w, right == "").
                if cut != len(w) and isP(right):
                    leftReversed = left[::-1]
                    if leftReversed in mappings:
                        # case 1 and 4
                        ans.append([a, mappings[leftReversed]])
        return ans

        '''
        2/2 A more straightforward translation of the 4 cases above.
        '''
        # case 1
        if "" in mappings:
            a = mappings[""]
            for b, w in enumerate(words):
                if isP(w) and a != b:
                    ans.append([a, b])
                    ans.append([b, a])
        # case 2
        for a, w in enumerate(words):
            r = w[::-1]
            if r in mappings:
                b = mappings[r]
                if a != b:
                    ans.append([a, b])
        # case 3 and 4
        for a, w in enumerate(words):
            for x in range(1, len(w)):
                left = w[:x]
                right = w[x:]
                rightReversed = right[::-1]
                if isP(left) and rightReversed in mappings:
                    ans.append([mappings[rightReversed], a])
                leftReversed = left[::-1]
                if isP(rightReversed) and leftReversed in mappings:
                    ans.append([a, mappings[leftReversed]])
        return ans