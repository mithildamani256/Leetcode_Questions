class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))
        
        # Reverse to process from right to left (least significant to most)
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                # 1. Multiply the digits
                digit_prod = int(num1[i1]) * int(num2[i2])
                
                # 2. Add it to what is ALREADY sitting at this position (including previous carries)
                total = digit_prod + res[i1 + i2]
                
                # 3. Update the current position with the single digit remainder
                res[i1 + i2] = total % 10
                
                # 4. Add the new carry to the NEXT position
                res[i1 + i2 + 1] += total // 10

        # Reverse back to normal order
        res = res[::-1]
        
        # Strip leading zeros
        beg = 0
        while beg < len(res) and res[beg] == 0:
            beg += 1

        return "".join(map(str, res[beg:]))