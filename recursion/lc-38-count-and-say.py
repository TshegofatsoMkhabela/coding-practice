class Solution:
    def encode(self, string):
        current_number = string[0]
        current_count = 0

        output = []
        for number in string:
            if number == current_number:
                current_count += 1
            else:
                output.append(f"{current_count}{current_number}")
                current_number, current_count = number, 1
        
        output.append(f"{current_count}{current_number}")
        return "".join(output)

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.encode(self.countAndSay(n - 1))
        