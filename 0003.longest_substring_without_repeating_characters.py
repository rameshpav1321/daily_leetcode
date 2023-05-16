class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        left,right=0,1
        my_set={s[left]:0}
        res=1
        while right<len(s):
            if s[right] in my_set:
                res=max(res,len(my_set))
                left=my_set[s[right]]+1
                my_set={}
                while left<right:
                    my_set[s[left]]=left
                    left+=1
            my_set[s[right]]=right
            res=max(res,len(my_set))
            right+=1
        return res