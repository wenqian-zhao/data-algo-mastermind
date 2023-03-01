"""
File:
Author: Wenqian Zhao
Description: Python3 solution to HZOJ-186-弹簧板
------------------
Result: 40 (Due to Dangerous Syscalls)
Time: 80ms
Memory: 8532kb
File size: 285b
------------------
"""

def f(i, arr):
    """
    1. 小球从i位置开始，被弹出去的次数
    2. i >= n -> 0
    3. f(i) = f(i+arr[i]) + 1
    """
    if i >= len(arr): return 0
    return f(i + arr[i], arr) + 1

def main():
    n = int(input())
    arr = list(map(int, input().split(" ")))
    print(f(0, arr))

main()
