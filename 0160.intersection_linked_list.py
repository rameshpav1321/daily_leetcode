class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        c1,c2=0,0
        tempA,tempB=headA,headB
        while tempA:
            c1+=1
            tempA=tempA.next
        while tempB:
            c2+=1
            tempB=tempB.next
        c=abs(c1-c2)
        while c>0:
            if c1>c2:
                headA=headA.next
                c-=1
            else:
                headB=headB.next
                c-=1
        while headA and headB:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next
        return None
