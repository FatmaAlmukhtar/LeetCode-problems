# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        stack = []
        dummy = head

        while head:
            stack.append(head.val)
            head = head.next

        while dummy:
            if stack.pop() != dummy.val:
                return False
            dummy = dummy.next

        return True
    """
        if not head or not head.next:
            return True

        # 1. Get the midpoint (slow)
        slow = fast = cur = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        # 2. Push the second half into the stack
        stack = [slow.val]
        while slow.next:
            slow = slow.next
            stack.append(slow.val)

        # 3. Comparison
        while stack:
            if stack.pop() != cur.val:
                return False
            cur = cur.next

        return True

      """
