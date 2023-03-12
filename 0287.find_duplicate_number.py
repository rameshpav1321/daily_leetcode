class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        one_jmp,two_jmp=0,0
        while True:
            one_jmp=nums[one_jmp]
            two_jmp=nums[nums[two_jmp]]
            if one_jmp==two_jmp:
                break
        one_jmp_left=0
        while True:
            one_jmp=nums[one_jmp]
            one_jmp_left=nums[one_jmp_left]
            if one_jmp==one_jmp_left:
                return one_jmp