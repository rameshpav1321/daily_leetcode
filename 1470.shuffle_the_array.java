class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] res=new int[2*n];
        int ind=0;
        for(int i=0;i<n;i++){
          res[ind]=nums[i];
          res[ind+1]=nums[i+n];
          ind+=2;
        }
        return res;
    }
}