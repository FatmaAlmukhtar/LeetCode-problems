# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        odd_dummy = odd_head = ListNode(0)
        even_dummy = even_head = ListNode(0)

        while head:
            odd_head.next = head
            even_head.next = head.next
            odd_head = odd_head.next
            even_head = even_head.next
            head = head.next.next if even_head else None

        odd_head.next = even_dummy.next

        return odd_dummy.next
