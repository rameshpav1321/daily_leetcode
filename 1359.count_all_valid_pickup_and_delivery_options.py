class Solution {
    public int countOrders(int n) {
        long res=1;
        for(int i =1;i<=n;i++){
            res*=i*(2*i-1);
            res%=1_000_000_007;
        }
        return (int)res;       
    }
}