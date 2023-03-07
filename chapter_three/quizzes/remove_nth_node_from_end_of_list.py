"""
Author: Wenqian Zhao
Description: 
Python3 solution to LeetCode-19-Remove_Nth_Node_From_End_of_List
"""


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return
        p, q = head, head
        for _ in range(n): 
            q = q.next
        if not q: 
            return head.next
        while q.next:
            q = q.next
            p = p.next
        if not p.next.next:
            p.next = None
            return head
        p.next = p.next.next
        return head