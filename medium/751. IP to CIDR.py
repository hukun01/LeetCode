# 751. IP to CIDR
class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        '''
        An IP has 8 * 4 = 32 bits
        Need to find the first 0 from the right, and if there is any 1 on the way,
        we need to cover this ip with 32;
        Leverage zfill(length) to match the binary length.
        Leverage int(str, 2) to make the str an integer in binary format.
        '''
        s = ''.join(bin(int(num))[2:].zfill(8) for num in ip.split('.'))
        ans = []
        while n > 0:
            for i in range(31 - s.rindex('1'), -1, -1):
                if 2 ** i <= n:
                    ans.append('.'.join(str(int(s[i:i + 8], 2)) for i in range(0, 32, 8)) + '/' + str(32 - i))
                    n -= 2 ** i
                    s = bin(int(s, 2) + 2 ** i)[2:].zfill(32)
                    break
        return ans