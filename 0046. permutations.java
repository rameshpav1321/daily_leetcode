class Solution {
    List<List<Integer>> res=new ArrayList<>();
    public void backtrack(LinkedHashSet<Integer> curr,int[] nums){
        if(curr.size()==nums.length){
            res.add(new ArrayList<>(curr));
            return;
        }
        for(int num:nums){
            if(!curr.contains(num)){
                curr.add(num);
                backtrack(curr,nums);
                curr.remove(num);
            }
        }


    }
    public List<List<Integer>> permute(int[] nums) {
        backtrack(new LinkedHashSet<>(),nums);
        return res;
    }
}