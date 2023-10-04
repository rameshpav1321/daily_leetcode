class Solution {
    public int minAddToMakeValid(String s) {
        Stack<Character> stack=new Stack<>();
        int count=0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='('){
                stack.push('(');
            }else if(s.charAt(i)==')' && stack.size()!=0){
                stack.pop();
            }else{count++;}
        }
        return (count+stack.size());
    }
}