// class Solution {
//     public int findLongestChain(int[][] pairs) {
//         Arrays.sort(pairs,(a,b)->a[1]-b[1]);
//         int prevMin=Integer.MIN_VALUE;
//         int res=0;
//         for (int[] pair:pairs){
//             if (pair[0]>prevMin){
//                 res++;
//                 prevMin=pair[1];
//             }
//         }
//         return res;
//     }
// }
class Solution {
    int dp(int i,HashMap<Integer,Integer> memo,int[][] pairs){
        int val=1;
        if(!memo.containsKey(i)){
            for (int j=i+1;j<pairs.length;j++){
                if (pairs[j][0]>pairs[i][1]){
                    val=Math.max(val,1+dp(j,memo,pairs));
                }
            }
            memo.put(i,val);
        }
        return memo.get(i);
    }
    public int findLongestChain(int[][] pairs) {
        HashMap<Integer,Integer> memo=new HashMap<>();
        int res=0;
        Arrays.sort(pairs,(a,b)->a[0]-b[0]);
        for(int i=0;i<pairs.length;i++){
            res=Math.max(res,dp(i,memo,pairs));
        }
        return res;
    }
}