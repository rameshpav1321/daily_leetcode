class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict={}
        for char in s:
            my_dict[char]=1+my_dict.get(char,0)
        for char in t:
            if char in my_dict:
                my_dict[char]-=1
            else:
                return False
        if all(value==0 for value in my_dict.values()):
            return True
        else:
            return False