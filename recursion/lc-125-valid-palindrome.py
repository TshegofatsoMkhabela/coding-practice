class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check(l_pointer, r_pointer, s):
            if l_pointer > r_pointer: return True
            if not s[l_pointer].isalnum(): return check(l_pointer + 1, r_pointer, s)
            if not s[r_pointer].isalnum(): return check(l_pointer, r_pointer - 1, s)

            if s[l_pointer].lower() != s[r_pointer].lower(): return False
            return check(l_pointer + 1, r_pointer - 1, s)
        return check(0, len(s) - 1, s)

