import sys
class Solution:
    def consecutive(self, num):
        '''
        we are looking for the number of prefixSum[i:j] so that it equals to num
        prefixSum[i:j] = prefixSum[:j] - prefixSum[:i] = num
        '''
        start = (num + 1) // 2
        ways = 0
        for i in range(start + 1, 1, -1):
            j = i
            total = 0
            while 0 < j and total < num:
                total += j
                j -= 1
            if total == num and i - j >= 2:
                ways += 1
        return ways

if __name__ == "__main__":
    so = Solution()
    for numStr in sys.argv[1:]:
        ans = so.consecutive(int(numStr))
        print(f"answer for {numStr}:", ans)