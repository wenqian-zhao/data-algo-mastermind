"""
File: recur_idx.py
Author: Wenqian Zhao
Description: Python3 solution to HZOJ-235-递归实现指数型枚举
"""

# ------------------My Solution------------------
# Result: 100
# Time: 44ms
# Memory: 7776kb
# File size: 231b
# -----------------------------------------------

def g(i, k,lst, n):
    if len(lst) > k + 1: return
    print(" ".join(lst))
    for j in range(i+1, n+1):
        g(j, k, lst + [str(j)], n)

def main():
    n = int(input())
    for i in range(1, n+1):
        g(i, n-i,[str(i)], n)

main()

# ---------------Official Solution---------------
# Result: 100
# Time: 76ms
# Memory: 8112kb
# File size: 355b
# -----------------------------------------------   
n_max = 10
arr = [1 for i in range(n_max)]

def print_one_result(n):
    for i in range(n):
        print(arr[i], end=" ")
    print(arr[n])

def f(i, j, n):
    """
    1. 在i位置最小值为j的情况下向后所能产出的所有指数型枚举
    2. 边界条件：当j>n: return
    3. f(i, j, n)
        (1) j + f(i+1, j+1, n) 
        (2) j+1 + f(i+1, j+2, n)
                  ...   
        (n) n + f(i+1, n+1, n) 
    """
    if j > n: return
    for k in range(j, n+1):
        arr[i] = k
        print_one_result(i)
        f(i+1, k+1, n)
    return


def main():
    n = int(input())
    f(0, 1, n)

main()