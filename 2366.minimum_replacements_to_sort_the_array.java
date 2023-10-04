class Solution {
    public long minimumReplacement(int[] nums) {
        int len=nums.length,prev=nums[len-1];
        long res=0;
        for(int i=len-2;i>=0;i--){
            int count=nums[i]/prev;
            if(nums[i]%prev!=0){
                count++;
                prev=nums[i]/count;
            }
            res+=count-1;
        }
        return res;      
    }
}