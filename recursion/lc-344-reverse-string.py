class Solution:
    def reverseString(self, s: list[str]) -> None:
        """ Do not return anything, modify s in-place instead."""
        def swap(l_pointer, r_pointer):
            if l_pointer < r_pointer: 
                s[l_pointer], s[r_pointer] = s[r_pointer], s[l_pointer]
                return swap(l_pointer + 1, r_pointer - 1)
        
        swap(0, len(s) - 1)
        