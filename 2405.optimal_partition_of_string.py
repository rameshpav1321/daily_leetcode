class Solution:
    def partitionString(self, s: str) -> int:
        sett = set()
        res = 0
        for char in s:
            if char not in sett:
                sett.add(char)
            else:
                res += 1
                sett.clear()
                sett.add(char)
        res += 1
        return res
