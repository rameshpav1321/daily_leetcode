class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [0, ""]
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub_string = s[i:j]
                if sub_string == sub_string[::-1] and len(sub_string) > res[0]:
                    res[0] = len(sub_string)
                    res[1] = sub_string
        return res[1]
