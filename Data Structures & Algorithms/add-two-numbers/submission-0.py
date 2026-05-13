# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Num = []
        l2Num = []

        curr = l1
        while curr:
            l1Num.append(curr.val)
            curr = curr.next
        curr = l2
        while curr:
            l2Num.append(curr.val)
            curr = curr.next
        i = len(l1Num) - 1
        num1 = 0
        while i >=0:
            num1+=int(l1Num[i] * (10 ** i))
            i-=1
        num2 = 0
        i = len(l2Num) - 1
        while i >=0:
            num2+=int(l2Num[i] * (10 ** i))
            i-=1
        sumNum = num1+num2

        digits = [int(digit) for digit in str(sumNum)]
        digits.reverse()

        dummy = ListNode(0)
        curr = dummy

        for digit in digits:
            curr.next = ListNode(digit)
            curr = curr.next
        return dummy.next




