# 1423. Maximum Points You Can Obtain from Cards
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''
        Find the min subarray sum with size (len(cardPoints) - k), this would be
        the part that we don't want to choose.
        '''
        s = len(cardPoints) - k
        minSum = math.inf
        currSum = 0
        for i in range(len(cardPoints)):
            currSum += cardPoints[i]
            if i - s >= 0:
                currSum -= cardPoints[i - s]
            if i + 1 >= s:
                minSum = min(minSum, currSum)
        return sum(cardPoints) - minSum