def hasCycle(self, head: Optional[ListNode]) -> bool:
        # nodesSeen = set() # a set is a data type that does not accept duplicates
        # while head is not None: # when head is None, you've reached end of linkedlist
        #     if head in nodesSeen:
        #         return True
        #     else:
        #         nodesSeen.add(head)
        #     head = head.next # move on to next node
        # return False
        one_jmp,two_jmp=head,head
        while two_jmp and two_jmp.next:
            one_jmp=one_jmp.next
            two_jmp=two_jmp.next.next
            if one_jmp==two_jmp:
                return True
        return False
      