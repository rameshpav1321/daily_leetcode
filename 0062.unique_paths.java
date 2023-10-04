class Solution {
     public int dp(int i, int j, int m, int n, HashMap<Pair<Integer, Integer>, Integer> map) {
        if (i == m && j == n) {return 1;}
        if (i > m || j > n) {return 0;}
        Pair<Integer, Integer> key = new Pair<>(i, j);
        if (!map.containsKey(key)) {
            int count = dp(i + 1, j, m, n, map) + dp(i, j + 1, m, n, map);
            map.put(key, count);
        }
        return map.get(key);
    }

    public int uniquePaths(int m, int n) {
        HashMap<Pair<Integer, Integer>, Integer> map = new HashMap<>();
        return dp(0, 0, m-1, n-1, map); 
    }
}