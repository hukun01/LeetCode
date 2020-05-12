# 169. Majority Element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Brute force approach is trivial. Here is the voting algorithm.
        We switch candidate to current number whenever its vote is 0.
        We will eventually switch to the majority number, because it has the most votes.
        '''
        vote = 0
        candidate = 0

        for num in nums:
            if vote == 0:
                candidate = num
            if num == candidate:
                vote += 1
            else:
                vote -= 1

        return candidate