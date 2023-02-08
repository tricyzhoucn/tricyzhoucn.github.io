---
title: java-base
date: 2023-02-08 08:47:05
tags: java
---

> java记录

<!-- more -->

## 1 基础

### 概念 

- **对象**：对象是类的一个实例，有状态和行为。例如，一条狗是一个对象，它的状态有：颜色、名字、品种；行为有：摇尾巴、叫、吃等。
- **类**：类是一个模板，它描述一类对象的行为和状态。
- **方法**：方法就是行为，一个类可以有很多方法。逻辑运算、数据修改以及所有动作都是在方法中完成的。
- **实例变量**：每个对象都有独特的实例变量，对象的状态由这些实例变量的值决定。

![java_intro](./java-base/java_intro.jpeg)



### 修饰符

访问控制修饰符：default，public，protected，private

非访问控制修饰符：final，abstract，static，synchronized

### 变量

局部变量

类变量（静态变量）

成员变量（非静态变量）

### 枚举

使用枚举类型限制变量只能使用预先设定好的值

```java
class FreshJuice{
    enum FreshJuiceSize{SMALL, MEDIUM, LARGE}
    FreshJuiceSize size;
}
public class HelloWorld {
    public static void main(String[] args){
        FreshJuice juice = new FreshJuice();
	juice.size = FreshJuice.FreshJuiceSize.MEDIUM;
    }
}
```

### 关键字

| 类别                 |    关键字    | 说明                           |
| :------------------- | :----------: | :----------------------------- |
| 访问控制             |   private    | 私有的                         |
|                      |  protected   | 受保护的                       |
|                      |    public    | 公共的                         |
|                      |   default    | 默认                           |
| 类、方法和变量修饰符 |   abstract   | 声明抽象                       |
|                      |    class     | 类                             |
|                      |   extends    | 扩充,继承                      |
|                      |    final     | 最终值,不可改变的              |
|                      |  implements  | 实现（接口）                   |
|                      |  interface   | 接口                           |
|                      |    native    | 本地，原生方法（非 Java 实现） |
|                      |     new      | 新,创建                        |
|                      |    static    | 静态                           |
|                      |   strictfp   | 严格,精准                      |
|                      | synchronized | 线程,同步                      |
|                      |  transient   | 短暂                           |
|                      |   volatile   | 易失                           |
| 程序控制语句         |    break     | 跳出循环                       |
|                      |     case     | 定义一个值以供 switch 选择     |
|                      |   continue   | 继续                           |
|                      |      do      | 运行                           |
|                      |     else     | 否则                           |
|                      |     for      | 循环                           |
|                      |      if      | 如果                           |
|                      |  instanceof  | 实例                           |
|                      |    return    | 返回                           |
|                      |    switch    | 根据值选择执行                 |
|                      |    while     | 循环                           |
| 错误处理             |    assert    | 断言表达式是否为真             |
|                      |    catch     | 捕捉异常                       |
|                      |   finally    | 有没有异常都执行               |
|                      |    throw     | 抛出一个异常对象               |
|                      |    throws    | 声明一个异常可能被抛出         |
|                      |     try      | 捕获异常                       |
| 包相关               |    import    | 引入                           |
|                      |   package    | 包                             |
| 基本类型             |   boolean    | 布尔型                         |
|                      |     byte     | 字节型                         |
|                      |     char     | 字符型                         |
|                      |    double    | 双精度浮点                     |
|                      |    float     | 单精度浮点                     |
|                      |     int      | 整型                           |
|                      |     long     | 长整型                         |
|                      |    short     | 短整型                         |
| 变量引用             |    super     | 父类,超类                      |
|                      |     this     | 本类                           |
|                      |     void     | 无返回值                       |
| 保留关键字           |     goto     | 是关键字，但不能使用           |
|                      |    const     | 是关键字，但不能使用           |

**注意：**Java 的 null 不是关键字，类似于 true 和 false，它是一个字面常量，不允许作为标识符使用。

### 继承

在 Java 中，一个类可以由其他类派生。如果你要创建一个类，而且**已经存在一个类具有你所需要的属性或方法**，那么你可以将新创建的类继承该类。

利用继承的方法，可以重用已存在类的方法和属性，而不用重写这些代码。被继承的类称为**超类**（super class），派生类称为**子类**（sub class）。

### 接口

在 Java 中，接口可理解为对象间相互通信的协议。接口在继承中扮演着很重要的角色。

接口**只定义派生要用到的方法**，但是方法的**具体实现完全取决于派生类**。

![java_exec](./java-base/java_exec.png)
