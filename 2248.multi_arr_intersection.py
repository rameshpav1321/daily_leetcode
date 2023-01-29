def intersection(self, nums: List[List[int]]) -> List[int]:
        my_dict={}
        for i in range(len(nums)):
            for num in nums[i]:
                my_dict[num]=1+my_dict.get(num,0)
        res=[]
        for key,val in my_dict.items():
            if val==len(nums):
                res.append(key)
        return sorted(res)