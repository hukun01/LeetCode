class Solution:
    def numberToWords(self, num: int) -> str:
        '''
        Need to process 'hundred' in multiple places, so it's better to do it in a function.
        Also need to handle billion, million, and thousand.
        '''
        data = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
        }
        
        # parse from 1 to 999
        def parse(number):
            hundreds = number // 100
            if hundreds > 0:
                ans.append(data[hundreds])
                ans.append("Hundred")
            number %= 100
            if number in data:
                ans.append(data[number])
                return
            elif (number // 10 * 10) in data:
                ans.append(data[number // 10 * 10])
            number %= 10
            if number > 0:
                ans.append(data[number])
        
        def divide(base, word):
            if base == 0:
                return
            nonlocal num
            if num >= base:
                parse(num // base)
                ans.append(word)
                num %= base
            
        ans = []
        divide(1000000000, "Billion")
        divide(1000000, "Million")
        divide(1000, "Thousand")
        parse(num)
        
        return ' '.join(ans) if ans else "Zero"