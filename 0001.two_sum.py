class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        my_dict={}
        for i in range(len(nums)):
            if target-nums[i] in my_dict:
                return [my_dict[target-nums[i]],i]
            else:
                my_dict[nums[i]]=i