class Solution(object):
    def fractionAddition(self, expression):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a)

        i = 0
        n = len(expression)

        num, den = 0, 1

        while i < n:
            # 1) read sign
            sign = 1
            if expression[i] == '+':
                i += 1
            elif expression[i] == '-':
                sign = -1
                i += 1

            # 2) read numerator
            a = 0
            while i < n and expression[i].isdigit():
                a = a * 10 + int(expression[i])
                i += 1
            a *= sign

            # 3) skip '/'
            i += 1  # expression[i] == '/'

            # 4) read denominator
            b = 0
            while i < n and expression[i].isdigit():
                b = b * 10 + int(expression[i])
                i += 1

            # 5) add to running fraction
            num = num * b + a * den
            den = den * b

            # 6) reduce
            g = gcd(num, den)
            num //= g
            den //= g

        return str(num) + "/" + str(den)
