---
title: linked-list
date: 2022-12-07 16:58:27
tags: 链表
---

> 链表相关汇总

<!-- more -->

### 总结

```python
#【去重】有序重复链表元素
def distinctLinkedList(head):
    dummy = head # 虚构指针指向头节点
    while head:
        while head.n and head.v == head.n.v:
            head.n = head.n.n
        head = head.n
    return dummy 
# 【删除】有序重复链表元素
def deleteLinkedList(head):
    dummy = ListNode(0)
    dummy.n = head # 虚构指针连接头结点
    head = dummy  # 头节点指向虚构节点
    while head.n and head.n.n: 
        if head.n.v == head.n.n.v: # 如果重复
            dv = head.n.v # 记录重复的值
            while head.n and head.n.v == dv: # 所有重复值
                head.n = head.n.n
        else:
            head = head.n
    return dummy.n    
# 翻转链表
def reverseLinkedList(head):
    if not head:
        return head
    dummy = head
    while head.n:
        next = head.n # 把头直连的节点摘出来
        head.n = head.n.n # 摘出来之后前后连上
        next.n = dummy # 摘出来的节点放到最前
        dummy = next # 摘出来的节点变为最前
    return dummy 
# 翻转链表第m到第n的节点
def reverseLinkedListMN(head,m,n):
    dummy = ListNode(0)
    dummy.n = head
    prev = dummy # 记录前面节点
    for _ in range(m-1): # 头结点走到m节点
        prev = prev.n
        head = head.n
    for _ in range(n-m): # head之后有n-m个节点要塞到前面
        next = head.n # 把头直连的节点摘出来
        head.n = head.n.n # 摘出来之后前后连上
        next.n = prev.n # 摘出来的节点放到需要翻转的节点最前(也就是prev之后)
        prev.n = next # prev连接最新翻转过来的节点
    return dummy.n   
# 翻转链表【回溯法】
def reverseLinkedListRecall(head):
    if not head: # 空链
        return head
    if not head.n: # 最后节点
        return head 
    next = reverseLinkedListRecall(head.n) # 取得最后节点只作最后返回用
    head.n.n = head # 翻转连接 左右都直连head head连接None
    head.n = None
    return next
  
class ListNode:
    def __init__(self, v, n=None):
        self.v = v
        self.n = n
x=ListNode(1)
y=ListNode(2)
x.n=y
print(x.v)
print(x.n.v)
```

