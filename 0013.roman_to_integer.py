class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res=roman_num_dict[s[-1]]
        for i in range(len(s)-2,-1,-1):
            if roman_num_dict[s[i]]<roman_num_dict[s[i+1]]:
                res-=roman_num_dict[s[i]]
            else:
                res+=roman_num_dict[s[i]]
        return res