"""
Author: Wenqian Zhao
Description: 
Python3 solution to LeetCode-92-Reverse_Linked_List_II
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left: int, right: int):
        if not head: return
        if left == right: return head
        return_val = head
        p, q = head, head.next

        if not q: return

        n = right - left
        
        for _ in range(n):
            q = q.next

        if left == 1:
            new_head, new_rear = self.reverse(p, n)
            new_rear.next = q
            return new_head
        q = q.next
        for _ in range(left - 2):
            q = q.next
            p = p.next
        new_head, new_rear = self.reverse(p.next, n)
        new_rear.next = q
        p.next = new_head
        return head
    
    def reverse(self, head, n):
        prev, cur = head, head.next
        for i in range(n):
            cur_next = cur.next
            cur.next = prev
            prev, cur = cur, cur_next
        
        return prev, head




