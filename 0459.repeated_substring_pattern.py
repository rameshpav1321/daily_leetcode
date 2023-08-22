class Solution:
    def chk_substring(self, s, sub_string):
        res = ""
        while len(res) < len(s):
            res += sub_string
        return res == s

    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)):
            if self.chk_substring(s, s[:i]):
                return True
        return False
