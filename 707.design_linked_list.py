class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size=-1
        
    def get(self, index: int) -> int:
        if index>self.size:
            return -1
        curr_ind=0
        curr_node=self.head
        if curr_ind==index:
            return curr_node.val
        else:
            while curr_ind<index:
                curr_ind+=1
                curr_node=curr_node.next
            return curr_node.val
        
    def addAtHead(self, val: int) -> None:
        if self.head:
            self.size+=1
            curr_head=self.head
            self.head=Node(val)
            self.head.next=curr_head
        else:
            self.size+=1
            self.head=Node(val)
        
    def addAtTail(self, val: int) -> None:
        if self.head:
            curr_node=self.head
            while curr_node.next!=None:
                curr_node=curr_node.next
            self.size+=1
            curr_node.next=Node(val)
        else:
            self.addAtHead(val)      

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size+1:
            return
        elif index==0:
            self.addAtHead(val)
        elif index==self.size+1:
            self.addAtTail(val)
        else:
            curr_ind=0
            curr_node=self.head
            while curr_ind<index:
                curr_ind+=1
                temp_node=curr_node
                curr_node=curr_node.next
            self.size+=1
            new_node=Node(val)
            new_node.next=curr_node
            temp_node.next=new_node
        
    def deleteAtIndex(self, index: int) -> None:
        if index>self.size:
            return
        curr_ind=0
        curr_node=self.head
        if curr_ind==index:
            self.size-=1
            self.head=curr_node.next
        else:
            while curr_ind<index:
                curr_ind+=1
                temp_node=curr_node
                curr_node=curr_node.next
            self.size-=1
            if curr_node.next:
                temp_node.next=curr_node.next
            else:
                temp_node.next=None
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)