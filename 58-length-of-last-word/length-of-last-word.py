class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        v = s.split(" ")
        return len(v[-1])