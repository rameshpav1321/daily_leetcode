class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet=new HashSet<>(wordDict);
        Queue<Integer> q=new LinkedList<>();
        boolean[] seen = new boolean[s.length() + 1];
        q.add(0);

        while(!q.isEmpty()){
            int start=q.remove();
            if(start==s.length()){return true;}
            for(int end=start+1;end<=s.length();end++){
                  if (seen[end]) {
                    continue;
                }
                if(wordSet.contains(s.substring(start,end))){
                q.add(end);
                seen[end] = true;
                }
            }
        }
        return false;
    }
}