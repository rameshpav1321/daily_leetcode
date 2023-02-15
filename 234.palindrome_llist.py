class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        curr=head
        while curr:
            stack.append(curr)
            curr=curr.next
        curr=head
        while stack:
            if curr.val!=stack.pop().val:
                return False
            curr=curr.next
        return True