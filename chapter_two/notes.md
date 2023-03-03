# 第2章：顺序表与链表
--- 
## 📖 顺序表


>### 结构讲解
- 结构定义
  - 一段连续的存储区：顺序表存储元素的地方
  - 变量size：顺序表大小
  - 变量count：存储元素的数量
- 操作：
  - 插入：
    - 将指定位置后的元素平行向后移动后插入
    - size不变，count + 1
  - 删除：
    - 将指定位置后的元素向前平移
    - size不变，count - 1


>### 代码演示
```python 
# !!!NOT TESTED!!!
class Vector:

    def __init__(self, size)
        self.size = size
        self.count = 0
        self.data = [None for _ in range(size)]
        return data

    def clear(self):
        if not self.data: return
        self.data = []
        self.size = 0
        self.count = 0
        return

    def insert(self, pos, val):
        if pos < 0 or pos > self.count: return 0
        if self.size == self.count and !self.expand(): return 0
        for i in range(self.count, pos-1):
            # 逆序遍历
            self.data[i+1] = self.data[i]
        self.data[pos] = val
        self.count += 1    
        return 1
    
    def erase(self, pos):
        if pos < 0 or pos >= self.count: return 0
        for i in range(pos+1, self.count):
            self.data[i-1] = self.data[i]
        self.count -= 1
        return 1

    def expand(self):
        if not self.data: return 0
        self.data = self.data + [None for _ in self.data]
        self.size *= 2
        return 1
```

---
## 📖 链表
--- 
>### 结构讲解
- 结构定义：链表是有若干个节点在逻辑结构上串联在一起，每个节点存储两部分信息，第一部分为数据信息，第二部分信息是将整个链表串联在一起的next指针，指向下一个链表节点的指针信息
- 结构操作：
  - 删除：指针直接跳过要被删除的节点
  - 插入
    - 建立指针p找到指向待插入位置的节点
    - 让新节点指向待插入位置之后的节点，并让指针p处的节点指向新节点
    - 程序内存信
- 两种链表：
  - 无头链表：程序内部使用一个指针指向第一个节点
  - 有头链表：程序内部使用一个虚拟头节点，不存储数据

>### 代码演示

```python
# 此代码由chatGPT生成，因为这个数据结构过于基础我就没有随着老师的课程听下去，如果有同学愿意测试这段代码并且进行补全将会十分感谢！

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def find(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next:
            current_node.next = current_node.next.next

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

```

>### 花式查找操作的实现 & 用有头链表改写插入操作

```python
# 懒 求补全
def 懒人大王():
    return “我本人”
```
>### 循环链表和双向链表
- 循环链表：
  - 在整个链表中最后一个节点指向第一个节点。
  - 头指针指向链表的最后一个节点，因为最后一个节点在循环链表中可以被当作一个虚拟头节点。插入时在n号位置插入节点就需要查找n次。
- 双向链表：
  - 在结构定义中，每一个节点除了向后的next指针外，还有一个向前的pre指针。





<div style="width:200px">
<hr/> <span style="font-family:Papyrus; font-size:1em;">Notes By Wenqian Zhao</span>
</div>
