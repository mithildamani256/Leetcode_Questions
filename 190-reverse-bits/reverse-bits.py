class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = bin(n)[2:].zfill(32)

        s = s[::-1]
        value = 0
        p = 0

        for i in range(len(s) - 1, -1, -1):
            current = int(s[i])
            value += (current * (2 ** p))
            p += 1

        return value
        