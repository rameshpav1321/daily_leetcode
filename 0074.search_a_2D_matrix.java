class Solution {
    public int binarySearch(int[] arr,int target){
        int left=0,right=arr.length-1;
        while(left<=right){
            int mid=(left+right)/2;
            if(arr[mid]==target){
                return mid;
            }else if(target<arr[mid]){
                right=mid-1;
            }else{
                left=mid+1;}
        }
        return right;
    }
    public boolean searchMatrix(int[][] matrix, int target) {
        int[] firstElements=new int[matrix.length];
        for(int i=0;i<matrix.length;i++){firstElements[i]=matrix[i][0];}
        int possibleRowIndex=binarySearch(firstElements,target);
        if(possibleRowIndex<0){return false;}else{
        int[] possibleRow=(target<matrix[possibleRowIndex][0] && possibleRowIndex>0)?matrix[possibleRowIndex-1]:matrix[possibleRowIndex];
        int possibleTargetIndex=binarySearch(possibleRow,target);
        return possibleRow[possibleTargetIndex]==target?true:false;
        }        
    }
}