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
        3. w1[0:k] is a P, w2 is the reversed w1[k:], then w2 + w1 is a P. This covers case 2 when k is 0.
        4. w1[k:] is a P, w2 is the reversed w1[0:k], then w1 + w2 is a P. This covers case 1 when k is len(w1).
        '''
        w_pos = {}
        for i, w in enumerate(words):
            w_pos[w] = i

        def is_palin(w):
            return w == w[::-1]

        ans = []
        for i, w in enumerate(words):
            for k in range(len(w)):
                p1 = w[:k]
                r_p1 = p1[::-1]
                p2 = w[k:]
                r_p2 = p2[::-1]
                # case 2 and 3
                if is_palin(p1) and r_p2 in w_pos and w_pos[r_p2] != i:
                    ans.append([w_pos[r_p2], i])
                # case 1 and 4, already checked cases for p2 == '' in above
                # condition, when p1 == w, r_p2 == ''.
                if p2 != '' and is_palin(p2) and r_p1 in w_pos and w_pos[r_p1] != i:
                    ans.append([i, w_pos[r_p1]])

        return ans

        '''
        2/2 A more straightforward translation of the 4 cases above.
        '''
        # case 1
        if "" in w_pos:
            a = w_pos[""]
            for b, w in enumerate(words):
                if is_palin(w) and a != b:
                    ans.append([a, b])
                    ans.append([b, a])
        # case 2
        for a, w in enumerate(words):
            r = w[::-1]
            if r in w_pos:
                b = w_pos[r]
                if a != b:
                    ans.append([a, b])
        # case 3 and 4
        for a, w in enumerate(words):
            for k in range(1, len(w)):
                p1 = w[:k]
                p2 = w[k:]
                r_p2 = p2[::-1]
                if is_palin(p1) and r_p2 in w_pos:
                    ans.append([w_pos[r_p2], a])
                r_p1 = p1[::-1]
                if is_palin(r_p2) and r_p1 in w_pos:
                    ans.append([a, w_pos[r_p1]])
        return ans