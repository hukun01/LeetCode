# 1423. Maximum Points You Can Obtain from Cards
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''
        We take cards from both ends, so the answer is the max
        subarray sum with size k after concatenating the last k cards to the
        head of the cards.
        A better approach is to find the min subarray sum with size (len(cardPoints) - k).
        '''
        c = cardPoints
        c = c[-k:] + c[:k]
        ans = 0
        r = 0
        for i in range(len(c)):
            r += c[i]
            if i - k >= 0:
                r -= c[i - k]
            ans = max(ans, r)
        return ans