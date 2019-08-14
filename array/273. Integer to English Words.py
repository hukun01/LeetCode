class Solution:
    def numberToWords(self, num: int) -> str:
        '''
        Need to process 'hundred' in multiple places, so it's better to do it recursively.
        Also need to handle billion, million, and thousand.
        '''
        oneToNine = {
            1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"
        }
        
        tenToNineteen = {
            10 :"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen",
            15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen"
        }
        
        twentyToNinety = {
            20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety"
        }
        
        def parseLessThanThousand(num):
            # only handles num from 1 to 999
            if num == 0:
                return
            if num >= 100:
                parseLessThanThousand(num // 100)
                ans.append("Hundred")
                parseLessThanThousand(num % 100)
            elif num in oneToNine:
                ans.append(oneToNine[num])
            elif num in tenToNineteen:
                ans.append(tenToNineteen[num])
            elif num in twentyToNinety:
                ans.append(twentyToNinety[num])
            else:
                ans.append(twentyToNinety[num // 10 * 10])
                ans.append(oneToNine[num%10])

        def transform(integer, word):
            if integer == 0:
                return
            nonlocal num
            if num >= integer:
                parseLessThanThousand(num // integer)
                ans.append(word)
                num = num % integer
        
        if num == 0:
            return "Zero"
        ans = []
        transform(1000000000, "Billion")
        transform(1000000, "Million")
        transform(1000, "Thousand")
        parseLessThanThousand(num)
        return ' '.join(ans)