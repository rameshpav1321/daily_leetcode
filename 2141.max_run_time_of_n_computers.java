public class Solution {
    public boolean checkRunTime(long time,int n,int[] batteries){
        long usage=0;
        for(int battery:batteries){
            usage+=Math.min(battery,time);
        }
        return usage>=(n*time)?true:false;
    }
    public long maxRunTime(int n, int[] batteries) {
        long left=1,right=Arrays.stream(batteries).asLongStream().sum()/n;
        while (left<right){
            // long mid=  right - (right - left) / 2;
            long mid=(left+right+1)/2;
            if(checkRunTime(mid,n,batteries)){
                left=mid;
            }else{
                right=mid-1;
            }
        }
        return left;     
    }
} 
