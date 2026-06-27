# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next        # move 1 step
            fast = fast.next.next   # move 2 steps

        return slow  # ← this was missing!