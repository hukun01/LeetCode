# 1641. Count Sorted Vowel Strings
class Solution:
    def countVowelStrings(self, n: int) -> int:
        '''
        1/2 Math.
        Imagine we are filling a n-elelment array with these 5 letters.
        We need to make 5 sections from the array, so that the letters can be
        placed in order.
        To make 5 sections, we need 4 bars.
        There are (n + 4) objects (n stars and 4 bars, see below reference) in
        the final arrangement, and we need to choose the positions for 4 bars.
        Before the 1st bar we put 'a', between the 1st and the 2nd bars we put
        'e', and so on.
        The number of bar combinations is the number of sorted vowel strings.
        Reference: https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics)
        '''
        k = 5
        num_separator = k - 1
        return math.comb(n + num_separator, num_separator)
        '''
        2/2 DP.
        Let f[i, char] be the count of i-length string ending at char
        f[i+1, char] = sum(f[i, smaller_char])
        '''
        vowels = 'aeiou'
        f = {char: 1 for char in vowels}
        for _ in range(2, n + 1):
            f2 = Counter()
            for char, count in f.items():
                for v in vowels:
                    if v >= char:
                        f2[v] += f[char]
            f = f2
        return sum(f.values())