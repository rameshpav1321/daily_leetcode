class Solution {
    HashMap<Integer,Integer> map=new HashMap<>();
    int dp(int[] nums,int target){
        if(target==0){return 1;}
        if(!map.containsKey(target)){
        int count=0;
        for(int i=0;i<nums.length;i++){
            if(target-nums[i]>=0){count+=dp(nums,target-nums[i]);}
        }
        map.put(target,count);
        }
        return map.get(target);

    }
    public int combinationSum4(int[] nums, int target) {
        return dp(nums,target);
    }
}