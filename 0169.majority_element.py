class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = {}
        for num in nums:
            my_dict[num] = 1 + my_dict.get(num, 0)
        res = sorted(my_dict, key=my_dict.get)
        return res[-1]
