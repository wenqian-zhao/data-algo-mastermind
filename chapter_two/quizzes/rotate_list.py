"""
Author: Wenqian Zhao
Description: 
Python3 solution to LeetCode-61-Rotate_List
"""
# brutal force
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return
        all_nodes = []
        while head:
            all_nodes.append(head)
            head = head.next
        k = k % len(all_nodes)
        all_nodes = all_nodes[-k:] + all_nodes[:-k]
        for i in range(len(all_nodes) - 1):
            all_nodes[i].next = all_nodes[i+1]
        all_nodes[-1].next = None
        return all_nodes[0]
    
# ---------------Bi-pointer------------------

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:return
        p = q = header = head
        k = k % length(head)
        for _ in range(k + 1): q = q.next
        while q:
            q = q.next
            p = p.next
        end = p.next if p.next else header
        while end.next:
            end = end.next
        end.next = header
        head = p.next
        p.next = None
        return head

def length(head):
    n = 0
    while head:
        n += 1
        head = head.next
    return n