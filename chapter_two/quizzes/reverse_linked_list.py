"""
File:
Author: Wenqian Zhao
Description: 
Python3 solution to LeetCode-206-Reverse_Linked_List
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return 
        prev, head = head, head.next
        prev.next = None
        while head:
            head_next = head.next
            head.next = prev
            prev, head = head, head_next
        return prev




