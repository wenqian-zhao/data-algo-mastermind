"""
File:
Author: Wenqian Zhao
Description: 
Python3 solution to LeetCode-141-Linked_List_Cycle
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        while head:
            if head in nodes: return True
            nodes.add(head)
            head = head.next
        return False

# ------------------------------------------------------------

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return 
        one_stepper, two_stepper = head, head.next
        while one_stepper and two_stepper:
            if one_stepper is two_stepper: return True
            one_stepper = one_stepper.next
            if two_stepper.next and two_stepper.next.next:
                two_stepper = two_stepper.next.next
            else: 
                return False
            
        return False


