class Solution {
    public ListNode[] splitListToParts(ListNode root, int k) {
        int len=0;
        ListNode curr=root;
        while(curr!=null){
            len++;
            curr=curr.next;
        }
        ListNode[] res=new ListNode[k];
        int partSize=len/k,extra=len%k;
        curr=root;
        for(int i=0;i<k;i++){
            ListNode head=new ListNode(0),write=head;
            for(int j=0;j<partSize+(i<extra?1:0);j++){
                write=write.next=new ListNode(curr.val);
                if(curr!=null){curr=curr.next;}
            }
            res[i]=head.next;
        }
       return res;
    }
}