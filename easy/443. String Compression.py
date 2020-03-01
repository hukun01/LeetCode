class Solution:
    def compress(self, chars: List[str]) -> int:
        '''
        
        '''
        idx = i = 0
        while i < len(chars):
            count = 0
            curr = chars[i]
            while i < len(chars) and chars[i] == curr:
                i += 1
                count += 1
            chars[idx] = curr
            idx += 1
            if count > 1:
                for c in str(count):
                    chars[idx] = c
                    idx += 1
        
        return idx