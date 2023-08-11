class Solution {
    public int countPairs(int threshold,int[] nums){
        int count=0;
        for(int i=1;i<nums.length;i++){
            if(nums[i]-nums[i-1]<=threshold){
                count++;
                i++;
            }
        }
        return count;      
    }
    public int minimizeMax(int[] nums, int p) {
        Arrays.sort(nums);
        int res=0;
        int low=0,high=nums[nums.length-1]-nums[0];
        while(low<=high){
            int mid=high-(high-low)/2;
            if(countPairs(mid,nums)>=p){
                res=mid;
                high=mid-1;
            }else{
                low=mid+1;
            }
        }
        return res;
    }
}