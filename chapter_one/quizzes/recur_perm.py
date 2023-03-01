"""
File: recur_perm.py
Author: Wenqian Zhao
Description: Python3 solution to HZOJ-236-递归实现排列型枚举
"""

# ---------------Python语法糖 AGAIN---------------
# Result: 100
# Time: 188ms
# Memory: 12836kb
# File size: 127b
# -----------------------------------------------
from itertools import permutations
n = int(input())
[print(" ".join(map(str, i))) for i in list(permutations(range(1, n+1)))]


# -------------------Solution--------------------
# Result: 100
# Time: 272ms	
# Memory: 7724kb
# File size: 297b
# -----------------------------------------------
n = int(input())
arr = [0 for _ in range(n)]
def f(i, j, n, s):
    if i == n: 
        print(" ".join(arr))
        return
    for k in range(1, n+1):
        if k not in s: 
            arr[i] = str(k)
            f(i+1, k+1, n, s + [k])

def main():
    f(0, 1, n, [])
    
main()