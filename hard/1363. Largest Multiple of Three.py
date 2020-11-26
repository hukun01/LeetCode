# 1363. Largest Multiple of Three
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        '''
        DP + bucket sort.
        The key observation: a number is multiple of 3, if and only if
        its sum of digits is multiple of 3.
        If the sum of digits mod 3 = 1, then the number mod 3 = 1 as well.

        Based on this, we get the sum of remainders from counts of 1, 4, 7
        that adds 1 to the remainder sum, and from counts of 2, 6, 8, that
        adds 2 to the remainder sum.
        If the remainder sum mod 3 == 1, then we need to either:
            1. remove 1 remainder that mod 3 = 1;
            2. remove 2 remainders that mod 3 = 2.
        If the remainder sum mod 3 == 2, similarly, we need to either:
            1. remove 2 remainder that mod 3 = 1;
            2. remove 1 remainder that mod 3 = 2.

        After this elimination process, all the left digits can form any
        numbers that are multiple of 3, we just need to pick the largest one.
        We want to put the largest digit at the front, so we will need to
        sort the digits, as we know there are at most 10 digits, so we can
        do bucket sort.
        Note that we add digits that mod 3 = 1 exactly remain1_count times.
        Similar logic applies to digits that mod 3 = 2.

        Time: O(n) where n is the length of digits array.
        Space: O(n).
        '''
        counts = [0] * 10
        for d in digits:
            counts[d] += 1
        remain1_count = counts[1] + counts[4] + counts[7]
        remain2_count = counts[2] + counts[5] + counts[8]
        remain_sum = (remain1_count + 2 * remain2_count) % 3
        if remain_sum == 1:
            if remain1_count >= 1:
                remain1_count -= 1
            else:
                remain2_count -= 2
        elif remain_sum == 2:
            if remain2_count >= 1:
                remain2_count -= 1
            else:
                remain1_count -= 2
        
        ans = []
        for d in range(9, -1, -1):
            if d % 3 == 0:
                while counts[d] > 0:
                    counts[d] -= 1
                    ans.append(str(d))
            elif d % 3 == 1:
                while counts[d] > 0 and remain1_count > 0:
                    remain1_count -= 1
                    counts[d] -= 1
                    ans.append(str(d))
            else:
                while counts[d] > 0 and remain2_count > 0:
                    remain2_count -= 1
                    counts[d] -= 1
                    ans.append(str(d))
        if len(ans) > 0 and ans[0] == '0':
            return '0'
        return ''.join(ans)