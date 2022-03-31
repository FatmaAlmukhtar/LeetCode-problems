# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


        head = ListNode(0)
        cur = head
        carry = 0

        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val = val1+val2+carry

            carry = val // 10

            # only take the first digit
            cur.next = ListNode(val%10)

            # update pointers
            cur = cur.next
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return head.next
