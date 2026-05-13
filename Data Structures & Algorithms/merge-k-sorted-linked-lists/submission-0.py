# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []
        for linkedList in lists:
            curr = linkedList
            while curr:
                nums.append(int(curr.val))
                curr = curr.next
        
        nums.sort()

        dummy = ListNode(0)
        node=dummy
        for num in nums:
            node.next = ListNode(num)
            node = node.next
        return dummy.next