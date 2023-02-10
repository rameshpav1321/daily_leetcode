class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy_node=Node(0)
        random_map={}
        curr,clone=head,dummy_node
        while curr:
            clone.next=Node(curr.val)
            random_map[curr]=clone.next
            curr,clone=curr.next,clone.next
        curr,clone=head,dummy_node.next
        while curr:
            clone.random=random_map[curr.random] if curr.random else None
            curr,clone=curr.next,clone.next    
        return dummy_node.next