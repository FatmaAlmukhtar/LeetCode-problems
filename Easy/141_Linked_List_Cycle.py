# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        res = False
        visited = set()
        visited.add(head)
        while head:
            head = head.next
            if head in visited:
                return True

            visited.add(head)
        
        return False
