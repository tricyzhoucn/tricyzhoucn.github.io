---
title: 求子数组相关
date: 2022-03-16 16:18:10
tags: 算法题
---

> 1.给定整数数组nums，给定元素个数n，求子数组？

<!-- more -->

#### 解法1：常规遍历

```python
def subsets(nums):
    output = [[]]
    for num in nums:
        for cur in output.copy():
            ext = cur + [num]
            output.append(ext)
        # output += [cur + [num] for cur in output] # 简化
    return output
print(subsets([1,2,3,4,5]))
```

#### 解法2: 位运算

```python
def subsets(nums):
    output = []
    for i in range(2**len(nums)):
        sub = []
        for j in range(len(nums)):
            if (i >> j) % 2 == 1: # 当前位1取0不取
                sub.append(nums[j])
        output.append(sub)
    return output
```

#### 解法3: 回溯

```python
def subsets(nums):
    res = []
    n = len(nums)
    def helper(i, tmp):
        res.append(tmp)
        for j in range(i, n):
            helper(j + 1, tmp+[nums[j]])
    helper(0, [])
    return res
print(subsets([1,2,3,4]))
```

> 变种1: 求子数组和可被整除

#### 解法：

```python
print(sum(map(lambda x:x%m==0, subsets(nums)[1:])))
# 优化:拆分&查找
mid = (len(nums)+1)/2
nums1 = nums[:mid]
nums1 = nums[mid:]
```



