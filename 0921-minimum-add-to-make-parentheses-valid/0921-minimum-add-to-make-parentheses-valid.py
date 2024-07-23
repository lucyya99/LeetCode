class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        a = []
        for p in s:
            if not a:
                a.append(p)
                continue
            if a[-1] == "(" and p == ")":
                a.pop()
            else:
                a.append(p)
        return len(a)