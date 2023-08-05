public class Solution {
    List<String> res=new ArrayList<>();
    Map<Character, String> map = Map.of(
        '2', "abc", '3', "def", '4', "ghi", '5', "jkl", 
        '6', "mno", '7', "pqrs", '8', "tuv", '9', "wxyz");
    public void backtrack(StringBuilder curr,int index,String digits){
        if(curr.length()==digits.length()){
            res.add(curr.toString());
            return;
        }
        String possibleChars=map.get(digits.charAt(index));
        for(char letter:possibleChars.toCharArray()){
            curr.append(letter);
            backtrack(curr,index+1,digits);
            curr.deleteCharAt(curr.length()-1);
        }
    }
    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) {
            return res;
        }
        backtrack(new StringBuilder(),0,digits);
        return res;        
    }
} {
    
}
