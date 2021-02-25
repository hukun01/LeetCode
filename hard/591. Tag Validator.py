# 591. Tag Validator
class Solution:
    def isValid(self, code: str) -> bool:
        '''
        Control flow and stack.
        Not hard, but need to cover each case carefully.

        Time: O(n) where n is len(code)
        Space: O(n)
        '''
        i = 0
        n = len(code)
        tag_stack = []
        top_level_block = 0 # Can't have <A></A><B></B>
        def get_tag(idx):
            tag = []
            while idx < n and code[idx] != '>':
                if not code[idx].isupper():
                    return False, None, idx
                tag.append(code[idx])
                idx += 1
            if not 1 <= len(tag) <= 9:
                return False, None, idx
            return True, ''.join(tag), idx + 1

        cdata_start = '![CDATA['
        cdata_end = ']]>'
        while i < n:
            if code[i] != '<':
                if not tag_stack: # all code needs to be wrapped in tags
                    return False
                i += 1
                continue
            i += 1
            if i == n:
                return False
            if code[i] == '!':
                # CDATA starts, and it needs to be wrapped in tags
                if not tag_stack:
                    return False
                if i + len(cdata_start) >= n or code[i:i+len(cdata_start)] != cdata_start:
                    return False
                i += len(cdata_start)
                while i + len(cdata_end) <= n and code[i:i+len(cdata_end)] != cdata_end:
                    i += 1
            elif code[i] == '/':
                # Closed tag
                good, tag_name, i = get_tag(i + 1)
                if not good or not tag_stack or tag_stack.pop() != tag_name:
                    return False

                if not tag_stack:
                    top_level_block += 1
            else:
                # Tag
                good, tag_name, i = get_tag(i)
                if not good:
                    return False
                tag_stack.append(tag_name)
        return len(tag_stack) == 0 and top_level_block == 1