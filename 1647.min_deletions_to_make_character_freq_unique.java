class Solution {
    public int minDeletions(String s) {
        char[] chars=s.toCharArray();
        Arrays.sort(chars);
        HashSet<Integer> set=new HashSet<>();
        int charCount=1,res=0;
        for(int i=1;i<=chars.length;i++){
            if(i<chars.length && chars[i]==chars[i-1]){
                charCount++;
            }else{
                while(set.contains(charCount)){
                    if(charCount==0){break;}
                    res++;
                    charCount--;
                }
                if(charCount!=0){set.add(charCount);}
                charCount=1;
            }
        }
        return res;
    }
}