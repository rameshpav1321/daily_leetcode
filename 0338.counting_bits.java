class Solution {
    public int countOnes(int num){
        int count=0;
        while(num>0){
            if(num%2==1){count++;}
            num/=2;
        }
        return count;
    }
    public int[] countBits(int n) {
        int[] res=new int[n+1];
        for(int i=0;i<=n;i++){
            res[i]=countOnes(i);
        }
        return res;
    }
}