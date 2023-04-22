class Solution:
    def removeDuplicates(self, lst: List[int]) -> int:
        index=1
        for i in range(1,len(lst)):     
            if lst[i]!=lst[i-1]:
                lst[index]=lst[i]
                index+=1
        return index