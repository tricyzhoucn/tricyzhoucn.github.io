---
title: sort-py
date: 2022-12-05 14:06:29
tags: 算法
---

> 排序算法汇总(基于python)

<!-- more -->

### 实现

```python
### 1 冒泡排序
### 双层循环，外层循环已冒泡元素个数，内层循环未冒泡元素与左侧对比
def bubbleSort(arr):
    for i in range(len(arr)): 
        for j in range(1,len(arr)-i): 
            if arr[j-1]>arr[j]: 
                arr[j-1],arr[j] = arr[j],arr[j-1]
    return arr
### 2 选择排序
### 双层循环，外层循环元素遍历，找到当前元素及之后元素最小值，交换当前元素和最小值元素
def selectSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr
### 3 插入排序
### 双层循环，外层未排序好元素开始(首位元素认为已排序)，如果小于左边记录索引和值，从后向前遍历已排序元素找到合适位置插入
def insertSort(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            index = i # 记录索引
            value = arr[i] # 记录值
            # 找位置(逐个后移)
            for j in range(i-1, -1, -1):
                if value<arr[j]:
                    arr[j+1]=arr[j]
                    index = j # 记录当前索引
                else:
                    break
            arr[index] = value # 插入
    return(arr)
### 4 希尔排序
### 逐渐减小步长，以步长长度插入排序，直至步长为1
def shellSort(arr):
    gap = len(arr)//2
    while gap>0:
        for i in range(gap, len(arr)):
            index = i
            value = arr[i]
            while index>=gap and arr[index-gap]>value:
                arr[index] = arr[index-gap]
                index = index-gap
            arr[index]=value
        gap = gap//2
    return arr
#### 5 归并排序
#### 逐步二分到长度为1 然后合并合并再合并
def mergeSort(arr):
    if len(arr)<=1:
        return arr
    m = len(arr)//2
    left = mergeSort(arr[:m])
    right = mergeSort(arr[m:])
    return merge(left,right)
def merge(left,right):
    l,r = 0,0 # 双指针
    result = []
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    result+=left[l:]
    result+=right[r:]
    return result
#### 6 快速排序
#### 三次遍历可以简化为一次 优化空间
def quickSort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    return quickSort(left) + middle + quickSort(right)
#### 7 堆排序
#### 先从非叶子结点开始递归堆化然后从后向前交换首尾去掉尾部从头开始重新堆化
def heapSort(arr):
    for i in range((len(arr)-2)//2, -1, -1): # 减1是为了长度转索引 再减1除2是为了找到非叶子节点(没有子节点都是)
        heapify(arr, i) # 堆化
    result = []
    for i in range(len(arr)-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i] # 交换首尾
        result.append(arr.pop(-1))  # 去除末尾
        heapify(arr, 0) # 重新堆化
    return result
def heapify(arr, i):
    smallest = i
    if 2*i+1<len(arr) and arr[2*i+1] < arr[smallest]:
        smallest = 2*i+1
    if 2*i+2<len(arr) and arr[2*i+2] < arr[smallest]:
        smallest = 2*i+2
    if not smallest==i: # 跟和子互换
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, smallest) # 子作为跟递归堆化
#### 8 计数排序
#### 有点浪费空间
def countSort(arr):
    count = [0]*(max(arr)-min(arr)+1)
    for a in arr:
        count[a-min(arr)]+=1
    result = []
    for i in range(len(count)):
        result += [i+min(arr)] * count[i]
    return result
arr = [1,5,3,2,0]
# bubbleSort(arr)
# selectSort(arr)
# insertSort(arr)
# shellSort(arr)
# mergeSort(arr)
# quickSort(arr)
# heapSort(arr)
countSort(arr)
```

### 参考

https://zhuanlan.zhihu.com/p/21839027
