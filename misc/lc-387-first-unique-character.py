class Solution:
    def firstUniqChar(self, s: str) -> int:
        characters = {}
        for character in s:
            characters[character] = characters.get(character, 0) + 1
        for character in characters:
            if characters[character] == 1:
                return s.index(character)
        return -1                
        