---
title: markdown-rule
date: 2022-01-23 17:13:37
tags:
---
markdown语法示例。

<!-- more -->

# 一级标题
## 二级标题
### 三级标题
#### 四级标题

# 无序列表
- 列表1
  - 列表1.1
  - 列表1.2
- 列表2
- 列表3
- 

# 引用
> 引用一段话

# 斜体和粗体
*斜体*

**粗体**

# 链接和图片
[链接](http://note.youdao.com/)

![图片](http://note.youdao.com/favicon.ico)

# 分割线
第一段
***
第二段

# 表格
| item | value |qty |
| :--- | ---:  |:--:|
|  w 1 | col 1 | 5  |
| w 2  | col 1 | 12 |

# 代码高亮
``` python
def main:
    print("123")

```

# todolist
- [x] 已完成项目
    - [x] 已完成事项1
    - [x] 已完成事项2
- [ ] 代办事项1

# 流程图
```
graph TD
    A[Christmas] -->B(Go shopping)
    B -->C{Let me think}
    C -->|One| D[Laptop]
    C -->|Two| E[iphone]
    C -->|Three| F[Car]
```

# 序列图
```
sequenceDiagram
    loop every day
        Alice->>John:Hello John, how are you?
        Jojn-->>Alice:Great!
    end
```

# 甘特图
```
gantt
dateFormat YYYY-MM-DD
title 产品计划表
section 初期阶段
明确需求:2016-03-01,10d
section 中期阶段
跟进开发:2016-03-11,15d
section 后期阶段
走查测试:2016-03-20,9d
```

# 数学公式
Inline math:`$dfrac{
\tfrac{1}{2}[1-(\tfrac{1}{2})^n] }{
    1-\tfrac{1}{2}} = s_n$`

[参考文档](https://blog.csdn.net/coolyoung520/article/details/108960281)

