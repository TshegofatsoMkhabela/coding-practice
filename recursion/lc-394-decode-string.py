class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for character in s:
            if character != ']':
                stack.append(character)
            else:
                curr_string = ""
                while stack and stack[-1].isalpha():
                    curr_string = stack.pop() + curr_string
                stack.pop()

                curr_number = ""
                while stack and stack[-1].isdigit():
                    curr_number = stack.pop() + curr_number
                
                stack.append(int(curr_number) * curr_string)
        return "".join(stack)
