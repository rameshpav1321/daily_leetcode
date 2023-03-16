class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        left_max_arr=[height[0]]
        right_max_arr=[height[-1]]
        for i in range(1,len(height)):
            left_max_arr.append(max(height[i],left_max_arr[i-1]))
            right_max_arr.append(max(height[len(height)-1-i],right_max_arr[i-1]))
        right_max_arr.reverse()
        for i in range(1,len(height)):
            res+=min(left_max_arr[i],right_max_arr[i])-height[i]
        return res