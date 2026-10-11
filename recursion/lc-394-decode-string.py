class Solution:
    def decodeString(self, s: str) -> str:
        self.idx = 0

        def decode():
            curr_number = 0
            output = ""

            while self.idx < len(s):
                character = s[self.idx]
                self.idx += 1

                if character.isdigit():
                    curr_number = curr_number * 10 + int(character)
                elif character == "[":
                    output += curr_number * decode()
                    curr_number = 0
                elif character == "]":
                    return output
                else:
                    output += character
            return output
        return decode()
    