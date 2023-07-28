class Solution {
    public boolean checkSpeed(int speed,int[] dist,double hour){
        double timeTaken=0;
        for(int i=0;i<dist.length;i++){
            double currTime=(double)dist[i]/speed;
            timeTaken+=(i==dist.length-1)?currTime:Math.ceil(currTime);
        }
        return timeTaken<=hour?true:false;
    }
    public int minSpeedOnTime(int[] dist, double hour) {
        int res=-1;
        int low=1;
        int high=10000000;
        while(low<=high){
            int mid=(low+high)/2;
            if (checkSpeed(mid,dist,hour)){
                res=mid;
                high=mid-1;
            }else{
                low=mid+1;
            }
        }
        return res;        
    }
}