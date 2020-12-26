# 1702. Maximum Binary String After Change
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        '''
        1/2 Bubble sort.
        The op2 will decrease the local number, but it's worth doing when it
        contributes to '00' which becomes '10' and increases the total number.

        This process is like bubble sort, a zero can bubble up to the left,
        once we have two zeros, we move the second zero to the left,
        virtually, then replace them by '10'. E.g., '1010' -> '1001' -> '1101

        Time: O(n) where n is len(binary)
        Space: O(n)
        '''
        arr = deque()
        n = len(binary)
        zeros = 0
        for a in binary:
            if a == '0':
                zeros += 1
                if zeros == 2:
                    arr.appendleft('1')
                    zeros -= 1
                else:
                    arr.append('0')
            else:
                arr.append('1')
        return ''.join(arr)
        '''
        2/2 A more concise process, based on bubble sort

        We don't have to do the process in 1/2 step by step, becaue we know in
        the final number, there's up to 1 zero, and all other zeros will be
        ones. The key is to find the lowest possible position of the single
        zero.
        We can't move the leftmost zero further left, but we can virtually
        push it right by gathering '00' and replacing with '10' like in 1/2.
        Overall, if the leftmost zero is at index 'start', all the 'k' ones in
        nums[start:] stay on the right, all zeros in nums[start:] will be
        moved left to meet the zero at 'start', and then we replace all zeros
        by '111..110', effectively push the only 0 to the right as far as
        possible.
        At the end, we have 'k' ones on the right, 'n-k-1' ones on the left,
        and one zero in the middle. If there is no zero in the input, just
        return the original input.
        '''
        if '0' not in binary: return binary
        n = len(binary)
        start = binary.find('0')
        k = binary.count('1', start)
        return '1' * (n - k - 1) + '0' + '1' * k