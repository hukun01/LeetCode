# 273. Integer to English Words
class Solution:
    scale2name = [
        (10 ** 9, 'Billion'), (10 ** 6, 'Million'), (10 ** 3, 'Thousand'), (10 ** 2, 'Hundred')
    ]

    num2name = {
        0: 'Zero',
        1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine',
        10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
        15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
        20: "Twenty", 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 
        60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'
    }

    def numberToWords(self, num: int) -> str:
        '''
        Recursion.

        The number is in recursive structure, so to use recursion to handle it.
        Specifically, since we have to hardcode all ~30 distinct number names,
        we can instantly return when input num matches any of these. Then we
        process the scales and their coefficient, during which we let recursion
        handle everything under 100, because numbers in [1, 100) consists of
        the distinct names above.

        For example, 234012 is Two Hundred Thirty Four Thousand Twelve, we
        process it by its scale, from large to small:
            f0(234012) -> f1(234) Thousand f0(12), recursion f1 handles '234'.
                f1(234) -> f2(2) Hundred f1(34), recursion f2 handles '2'.
                    2 -> it's simple num, we return 'Two'
                    f1(34) -> simple enough, we return 'Thirty Four'
                f1(234) -> Two Hundred Thirty Four
            f0(12) is also simple (we have to hard code [10 to 20] anyway)
            f0(234012) -> Two Hundred Thirty Four Thousand Twelve

        Time: O(1) because number is limited at most 32 bits.
        Space: O(1)
        '''
        f = self.numberToWords

        if num in Solution.num2name:
            return Solution.num2name[num]

        # num must be >= 21 to pass the above check, so (num // 10 * 10) is non-zero.
        if num < 100:
            return f'{f(num // 10 * 10)} {f(num % 10)}'

        ans = []
        for s, name in Solution.scale2name:
            if num >= s:
                ans.append(f(num // s))
                ans.append(name)
                num %= s

        if num > 0:
            ans.append(f(num))

        return ' '.join(ans) or "Zero"