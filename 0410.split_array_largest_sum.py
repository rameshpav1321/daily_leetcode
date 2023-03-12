def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        res=0
        while low<=high:
            mid=(low+high)//2
            aux_k=1
            aux_sum=0
            for i in range(len(nums)):
                if aux_sum+nums[i]>mid:
                    aux_k+=1
                    aux_sum=nums[i]
                else:
                    aux_sum+=nums[i]
            if aux_k<=k:
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res