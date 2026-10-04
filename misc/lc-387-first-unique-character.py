class Solution:
    def firstUniqChar(self, s: str) -> int:
        for idx, character in enumerate(s):
            if character not in s[idx+1:] + s[:idx]:
                return idx
        return -1
