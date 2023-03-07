"""
Author: Wenqian Zhao
Description: 
Python3 solution to LeetCode-142-Linked_List_Cycle_II

"""
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = p2 = p3 = head
        n = 0
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
            if not p2: return None
            p2 = p2.next
            if p1 is p2:
                break
        while p1 and p3:
            if p1 is p3:
                return p1
            p1 = p1.next
            p3 = p3.next
            n += 1