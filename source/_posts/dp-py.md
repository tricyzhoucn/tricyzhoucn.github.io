---
title: dp-py
date: 2022-12-09 15:13:30
tags: 动态规划
---

> 动态规划问题汇总

<!-- more -->

### 背包

```python
# 01背包
# dp[i][j]表示在0~i下标物品中选取，在总承重0~j的情况下获得的【最大重量】；
# w[i]表示第i件的物品的重量，对应到索引上是i-1
# 状态转移方程:f[i][j] = max(f[i-1][j], f[i-1][j-w[i]] + w[i])
def backpack1(m, w):
    dp = [[0]*(m+1) for _ in range(len(w)+1)]
    for i in range(1, len(w)+1):
        for j in range(1, m+1):
            if w[i-1]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+w[i-1])
    return dp[-1][-1]
# 01背包
# dp[i][j]表示在0~i下标物品中选取，在总承重0~j的情况下获得的【最大价值】；
# w[i]表示第i件的物品的重量，v[i]表示第i件的物品的重量, 对应到索引上是i-1
# 状态转移方程:f[i][j] = max(f[i-1][j], f[i-1][j-w[i]] + v[i])
def backpack2(m, w, v):
    dp = [[0]*(m+1) for _ in range(len(w)+1)]
    for i in range(1, len(w)+1):
        for j in range(1, m+1):
            if w[i-1]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+v[i-1])
    return dp[-1][-1]
# 优化空间复杂度
def backpack3(m, w, v):
    dp = [0]*(m+1) # 只占用m+1长度内存
    for i in range(1, len(w)+1): # 遍历物品
        for j in range(m, 0, -1): # 逆序遍历 上轮前面dp[j-w[i-1]]还要用
            if w[i-1]<=j: # 如果可以放下
                dp[j] = max(dp[j], dp[j-w[i-1]] + v[i-1])
    return dp[-1]
backpack1(10, [3,4,8,5])
backpack2(10, [3,4,8,5], [10,4,5,2])
backpack3(10, [3,4,8,5], [10,4,5,2])
```

### 爬楼梯

```python
# 爬楼梯 n阶楼梯，可以选择上1阶或2阶共有多少种方法
# 1.递归
def climb1(n):
    if n<=2:
        return n
    return climb1(n-1) + climb1(n-2)
# climb1(10)

# 2.动态规划
# 状态转移方程：f[i] = f[i-1] + f[i-2]
def climb2(n):
    dp = [0]*n
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[-1]
# climb2(10)
```

