"""
File: recur_combo.py
Author: Wenqian Zhao
Description: Python3 solution to HZOJ-236-递归实现组合型枚举
"""

# ------------------Python语法糖 XD---------------
# Result: 100
# Time: 152ms
# Memory: 7816kb
# File size: 152b
# -----------------------------------------------
from itertools import combinations
n, m = list(map(int, input().split()))
[print(" ".join(map(str, i))) for i in list(combinations(range(1, n+1), m))]


# -------------------Solution--------------------
# Result: 100
# Time: 184ms
# Memory: 7696kb
# File size: 308b
# -----------------------------------------------
n, m = list(map(int, input().split()))
arr = [0 for _ in range(m)]
def f(i, j, n):
    if i == m: 
        print(" ".join(arr))
        return
    for k in range(j, n+1):
        if n - k < m - i - 1: return
        arr[i] = str(k)
        f(i+1, k+1, n)

def main():
    f(0, 1, n)
    
main()