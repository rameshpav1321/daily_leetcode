class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev,curr=None,node
        while curr.next:
            curr.val,curr.next.val=curr.next.val,curr.val
            prev=curr
            curr=curr.next
        prev.next=None
        # or can be done this way
        # node.val = node.next.val
        # node.next = node.next.next