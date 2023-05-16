class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict={}
        for num in nums:
            my_dict[num]=1+my_dict.get(num,0)
        sorted_dict=sorted(my_dict.items(),key=lambda x:x[1],reverse=True)
        res=[]
        for i in range(k):
            res.append(sorted_dict[i][0])
        return res