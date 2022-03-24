# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val < list2.val:
            head = merged = ListNode(list1.val)
            list1 = list1.next
        else:
            head = merged = ListNode(list2.val)
            list2 = list2.next

        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next

            head = head.next

        if list1:
            head.next = list1
        elif list2:
            head.next = list2

        return merged
