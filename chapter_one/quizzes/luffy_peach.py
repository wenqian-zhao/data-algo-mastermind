"""
File: luffy_peach.py
Author: Wenqian Zhao
Description: Python3 solution to HZOJ-184-路飞吃桃
------------------
Result: 100
Time: 140ms
Memory: 7760kb
File size: 88b
------------------
"""

def f(n):
    '''
    1. f(n): 能吃n天的桃子数量
    2. n == 1 -> 1
    3. (f(n - 1) + 1) * 2 = f(n)
    '''
    if n == 1: return 1
    return 2 * (f(n - 1) + 1)

def main():
    n = int(input())
    print(f(n))

main()