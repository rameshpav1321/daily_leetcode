class Solution {
    List<List<Integer>> res=new ArrayList<>();
    public void backtrack(List<Integer> curr,int start,int n,int k){
        if(curr.size()==k){
            res.add(new ArrayList<>(curr));
            return;
        }
        for(int i=start;i<=n;i++){
            curr.add(i);
            backtrack(curr,i+1,n,k);
            curr.remove(curr.size()-1);
        }
        return;
    }
    public List<List<Integer>> combine(int n, int k) {
        backtrack(new ArrayList<Integer>(),1,n,k);
        return res;       
    }
}