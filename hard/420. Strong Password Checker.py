# 420. Strong Password Checker
class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        '''
        Control flow.
        Analyze case by case.
        1. When len(s) < 6, we need to add x = (6 - len(s)) chars to s, and
        ensure we have all 3 types of chars. If x >= 3, we can add 3 types of
        chars if we don't have them; if x < 3, we need to add the 
        max(missing_type, x).
        2. When 6 <= len(s) <= 20, we don't need to add or delete, replace can
        fix all issues. Find out all consecutive chars, for each such sequence
        y, we need len(y) // 3 replace to fix it. We still need to ensure
        there's no missing types, so we need max(missing_type, replace).
        3. When len(s) > 20, we need to delete and maybe also replace. Note
        that although replace is more efficient at fixing consecutive chars,
        if we have to delete, we can use delete to fix consecutive chars as
        well, so we don't need to use replace as additional operations.
        For a sequence with len % 3 == 0, we can reduce one triplet(also a
        replace operation) by deleting 1 char;
        For a sequence with len % 3 == 1, we can reduce one triplet by
        deleting 2 chars.
        For the remaining ones, we can reduce one triplet by deleting 3 chars.
        '''
        missing_type = 3
        if any('a' <= c <= 'z' for c in s): missing_type -= 1
        if any('A' <= c <= 'Z' for c in s): missing_type -= 1
        if any(c.isdigit() for c in s): missing_type -= 1

        # Let 'one' be the number of consecutive sequences whose replace
        # operations can be reduced by deleting one char.
        # Similar to the definition of 'two', except we delete 2 chars.
        replace = one = two = 0
        p = 2
        n = len(s)
        while p < n:
            if s[p] == s[p-1] == s[p-2]:
                length = 2
                while p < n and s[p] == s[p-1]:
                    length += 1
                    p += 1
                    
                replace += length // 3
                if length % 3 == 0: one += 1
                elif length % 3 == 1: two += 1
            else:
                p += 1

        if n < 6:
            return max(missing_type, 6 - n)
        elif n <= 20:
            return max(missing_type, replace)

        delete_cache = delete = n - 20

        replace -= min(delete, one)
        delete = max(0, delete - one)
        replace -= min(delete, two * 2) // 2
        delete = max(0, delete - two * 2)
        replace -= delete // 3

        return delete_cache + max(missing_type, replace)