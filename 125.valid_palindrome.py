class Solution:
    def isPalindrome(self, s: str) -> bool:
        str=''.join(char.lower() for char in s if char.isalnum())
        for i in range(len(str)//2):
            if str[i]!=str[~i]:
                return False
        return True