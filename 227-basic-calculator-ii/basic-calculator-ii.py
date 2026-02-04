class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        sign = '+'
        
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + (ord(ch) - ord('0'))
            
            # If operator or end of string (ignore spaces)
            if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:  # sign == '/'
                    prev = stack.pop()
                    stack.append(int(prev / float(num)))  # truncate toward 0
                
                sign = ch
                num = 0
        
        return sum(stack)
