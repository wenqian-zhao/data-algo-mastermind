"""
Author: Wenqian Zhao
Description: 
Python3 solution to LeetCode-202-Happy_Number
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        out = set()
        while True:
            if n in out: 
                return False
            out.add(n)
            digit_sum = 0
            while n >= 10:
                n, q = divmod(n, 10)
                digit_sum += q ** 2
            digit_sum += n ** 2
            if digit_sum == 1: 
                return True
            n = digit_sum
        return False
    
# --------------------------------------------------------

class Solution:
    def isHappy(self, n: int) -> bool:
        p = q = n
        while q != 1:
            q = get_next(get_next(q))
            p = get_next(p)
            if p == q and q != 1:
                return False 
        return True
    
def get_next(n):
    digit_sum = 0
    while n >= 10:
        n, q = divmod(n, 10)
        digit_sum += q ** 2
    digit_sum += n ** 2
    return digit_sum

