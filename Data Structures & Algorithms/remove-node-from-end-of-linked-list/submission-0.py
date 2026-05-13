# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None
        i=1

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
    
        rev_head = prev
        curr = prev
        prev = None
        while curr and i<=n:
            temp = curr.next
            if i==n:
                if prev:
                    prev.next = temp
                else:
                   rev_head = temp 
            prev = curr
            curr = temp
            i+=1
        
        curr = rev_head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev