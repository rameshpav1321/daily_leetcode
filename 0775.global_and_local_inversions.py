def isIdealPermutation(self, nums: List[int]) -> bool:
        # for i in range(len(nums)-2):
        #     for j in range(i+2,len(nums)):
        #         if nums[i]>nums[j]:
        #             return False
        # return True
        ###############################################
        # min_val=nums[-1]
        # for i in range(len(nums)-1,1,-1):
        #     min_val=min(min_val,nums[i])
        #     if nums[i-2]>min_val:
        #         return False
        # return True
        ################################################
        for i in range(len(nums)):
            if abs(nums[i]-i)>1:
                return False
        return True
