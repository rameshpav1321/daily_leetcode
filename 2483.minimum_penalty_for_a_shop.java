class Solution {
    public int bestClosingTime(String customers) {
        int len=customers.length();
        int currPenalty=0;
        for(int i=0;i<len;i++){
            if(customers.charAt(i)=='N'){currPenalty++;}
        }
        int minPenalty=currPenalty,res=len;
        for(int i=len-1;i>=0;i--){
            if(customers.charAt(i)=='Y'){currPenalty++;}
            else{currPenalty--;}
            if(currPenalty<=minPenalty){
                minPenalty=currPenalty;
                res=i;
                }
        }
        return res;
    }
}