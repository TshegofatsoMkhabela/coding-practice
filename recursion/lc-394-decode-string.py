class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_word = []
        curr_number = ""
        for character in s:
            if character != ']':
                stack.append(character)
                continue
            while stack[-1].isalpha():
                curr_word.append(stack.pop())
            if stack[-1] == '[':
                stack.pop()
                while stack and stack[-1].isdigit():
                    curr_number = stack.pop() + curr_number
            stack.append("".join(int(curr_number) * curr_word[::-1]))
            curr_word, curr_number = [], ""
        return "".join(stack)
