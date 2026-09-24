class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        Math.
        Converting to string is trivial, let's use math.
        Build a new number by visiting x's last digit and dividing x by 10 each time.
        If the new number is the same as the original x, that means the x reads the same
        forward and backward, aka, it's a palindrome.
        '''
        inputNum = x
        newNum = 0
        while x > 0:
            newNum = newNum * 10 + x % 10
            x = x // 10
        
        return newNum == inputNum
