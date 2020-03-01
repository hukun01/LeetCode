class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        Two approaches. One is recursion with backtracking, another is iterative.
        '''
        '''
        allComb = [""] if digits else []
        for d in digits:
            currComb = []
            for comb in allComb:
                for letter in data[d]:
                    currComb.append(comb + letter)
            allComb = currComb
        
        return allComb
        '''
        if not digits:
            return []
        
        data = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        
        answer = []
        currLetters = []
        def dfs(idx, curr):
            if idx == len(digits):
                answer.append(''.join(currLetters))
                return
            for letter in data[digits[idx]]:
                currLetters.append(letter)
                dfs(idx + 1, currLetters)
                currLetters.pop()
        
        dfs(0, "")
        return answer