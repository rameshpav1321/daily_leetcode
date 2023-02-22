class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater={nums2[-1]:-1}
        stack=[nums2[-1]]
        for i in range(len(nums2)-2,-1,-1):
            if nums2[i]<stack[-1]:
                next_greater[nums2[i]]=stack[-1]
            else:
                while stack and stack[-1]<nums2[i]:
                    stack.pop()
                next_greater[nums2[i]]=stack[-1] if len(stack) else -1
            stack.append(nums2[i])
        res=[]
        for num in nums1:
            res.append(next_greater[num])
        return res