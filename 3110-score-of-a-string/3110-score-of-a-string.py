class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(0, len(s)-1):
            sum += abs(ord(s[i+1]) - ord(s[i]))
        return sum