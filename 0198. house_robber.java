class Solution {
    HashMap<Integer,Integer> res=new HashMap<>();
    public int dp(int houseIndex,int[] nums){
        if(houseIndex==0){return nums[houseIndex];}
        if(houseIndex==1){return Math.max(nums[houseIndex],nums[houseIndex-1]);}
        if(!res.containsKey(houseIndex)){
        res.put(houseIndex,Math.max(dp(houseIndex-2,nums)+nums[houseIndex],dp(houseIndex-1,nums)));
        }
        return res.get(houseIndex);
    }
    public int rob(int[] nums) {
        return dp(nums.length-1,nums);
    }
}