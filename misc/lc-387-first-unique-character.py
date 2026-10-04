class Solution:
    def firstUniqChar(self, s: str) -> int:
        characters = {}
        for character in s:
            if character not in characters:
                characters[character] = 1
            else:
                characters[character] += 1
        for character in characters:
            if characters[character] == 1:
                return s.index(character)
        return -1
