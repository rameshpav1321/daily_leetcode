class Solution {
    Map<Integer,Integer> map=new HashMap<>();
    public int dp(int stairIndex,int[] cost){
        if(stairIndex<2){return cost[stairIndex];}
        if(!map.containsKey(stairIndex)){
            map.put(stairIndex,cost[stairIndex]+Math.min(dp(stairIndex-1,cost),dp(stairIndex-2,cost)));
        }
        return map.get(stairIndex);

    }
    public int minCostClimbingStairs(int[] cost) {
        return Math.min(dp(cost.length-1,cost),dp(cost.length-2,cost));
    }
}