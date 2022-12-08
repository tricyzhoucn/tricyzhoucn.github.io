---
title: binary-tree
date: 2022-12-08 14:20:24
tags: 树
---

> 树相关汇总

<!-- more -->

### 普通遍历

```python
# 前序遍历(根左右)
def preOrderTravesal(root):
    if not root:
        return
    print(root.v)
    preOrderTravesal(root.l)
    preOrderTravesal(root.r)
# 中序遍历(左根右)
def inOrderTravesal(root):
    if not root:
        return
    inOrderTravesal(root.l)
    print(root.v)
    inOrderTravesal(root.r)
# 后续遍历(左右根)
def posOrderTravesal(root):
    if not root:
        return
    posOrderTravesal(root.l)
    posOrderTravesal(root.r)
    print(root.v)

# 非递归前序遍历
def preOrder(root):
    if not root:
        return None
    result = [] # 结果
    stack = []  # 缓存
    while root!=None or len(stack)!=0: 
        while root!=None: # 遍历左子树
            result.append(root.v) # 根结点先入结果集
            stack.append(root)
            root = root.l
        node = stack[len(stack)-1] # 弹出
        stack = stack[:len(stack)-1] # 清理缓存
        root = node.r # root为弹出节点的右节点
    return result

# 非递归中序遍历
def inOrder(root):
    if not root:
        return None
    result = []
    stack = []
    while root!=None or len(stack)!=0:
        while root!=None:
            stack.append(root)
            root = root.l
        node = stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        result.append(node.v) # 左节点先入结果集(和前序区别)
        root = node.r
    return result

# 非递归后序遍历
def posOrder(root):
    if not root:
        return None
    result = []
    stack = []
    lastVisit = None
    while root!=None or len(stack)!=0:
        while root!=None:
            stack.append(root)
            root = root.l
        node = stack[len(stack)-1]
        if node.r==None or node.r==lastVisit: # 确保右节点先于跟节点进入结果集
            stack = stack[:len(stack)-1] 
            result.append(node.v) 
            lastVisit = node
        else:
            root = node.r # 确保右节点先于跟节点进入结果集
    return result
```

### 优先遍历

```python
# 深度优先遍历(前序遍历)
result = []
def dfs(root):
    if root==None:
        return
    result.append(root.v)
    dfs(root.l)
    dfs(root.r)
# 广度优先遍历(层次遍历)
def bfs(root):
    if root==None:
        return 
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node.v)
        if node.l: queue.append(node.l)
        if node.r: queue.append(node.r)
    return result
```

### 变种

```python
# 最大深度
def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.l), maxDepth(root.r))+1
 
# 是否平衡树(平衡返回最大深度)
# 平衡树:左右子树深度差不超过1
def balanceTree(root):
    if not root:
        return 0
    left = maxDepth(root.l)
    right = maxDepth(root.r)
    if abs(left-right)>1:
        return -1
    return max(left,right)+1
 
# 最大路径值和
result = float("-inf")
def maxPathSum(root):
    if not root:
        return 0
    left = maxPathSum(root.l)
    right = maxPathSum(root.r)
    global result
    result = max(left + right + root.v, result) # 如果当前节点为根节点最大路径和
    return max(0, max(left, right) + root.v) # 当前节点作为子节点能提供的最大路径和
maxPathSum(n1)
print(result)

# 公共祖先
def commonAncester(root, p, q):
    if not root or root==p or root==q:
        return root
    left = commonAncester(root.l, p, q) # 是否包含p或q
    right = commonAncester(root.r, p, q)
    if not left: return right # 没在左说明在右
    if not right: return left # 没在右说明在左
    return root # 左右都有说明跟节点是公共祖先
commonAncester(n1,n2,n3).v

# 是否是二叉搜索树
def bst(root):
    def helper(root, minv, maxv):
        if not root:
            return True
        if not minv<root.v<maxv:
            return False
        return helper(root.l, minv, root.v) and helper(root.r, root.v, maxv)
    return helper(root, float("-inf"), float("inf"))
bst(n1)

# 插入bst
def insertBST(root, v):
    if not root:
        return TreeNode(v)
    if root.v < v:
        root.r = insertBST(root.r, v)
    if root.v > v:
        root.l = insertBST(root.l, v)
    return root
```

### 建树

```python
class TreeNode:
    def __init__(self, v, l, r):
        self.v = v
        self.l = l
        self.r = r
n1,n2,n3,n4,n5,n6,n7 = TreeNode(1,None,None),TreeNode(2,None,None),TreeNode(3,None,None),TreeNode(4,None,None),TreeNode(5,None,None),TreeNode(6,None,None),TreeNode(7,None,None)
n1.l=n2
n1.r=n3
n2.l=n4
n2.r=n5
n3.l=n6
n3.r=n7
#    1
#  2   3
# 4 5 6 7
# 3层 长度7 非子节点最大索引7/2
n1.r.r.v
```

