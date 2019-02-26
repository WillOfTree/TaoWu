#coding = utf-8


class Node(object):
    '''节点'''

    def __init__(self, ele):
        self.element = ele
        self.next = None


class SingleLinkList(object):
    '''单链表'''

    def __init__(self, node=None):
        # 头节点
        self.__header = node

    def is_emport(self):
        '''判断是否为空'''
        return self.__header == None

    def length(self):
        '''读取长度'''

        cur = self.__header
        # 判断链表是否为空
        if !self.is_emport:
            return 0

        lenth = 0
        while True:
            lenth += 1
            cur = cur.next
            # 如果链条为指向空，退出
            if cur.next == None:
                break

        return lenth

    def travel(self):
        '''遍历表'''

        cur = self.__header
        while cur.next != None:
            print(cur.element, end=" ")
            cur = cur.next

    def add(self, item):
        '''头部添加元素'''

        cur = Node(item)
        # 切换指向
        # ago_next = cur.next
        # self.header.next = item
        # item.next = ago_next
        item.next, cur.next = cur.next, item

    def append(self, item):
        '''尾部添加'''

        cur = Node(item)
        while True:
            if cur.next == None:
                cur.next = item
                break
            else:
                cur = cur.next

    def insert(self, path, item):
        '''指定位置添加'''
        cur = Node(item)
        # 小于链表
        if path < 0:
            path = 0
        # 大于链表

        for i in range(path + 1):
            if i == path:
                cur.next, item.next = item, cur.next
            cur = cur.next

    def remove(self, item):
        '''删除第几个节点'''
        cur = self.__header
        for i in range(item):
            if i == item:
                cur.next = cur.next.next

    def search(self, item):
        '''查找结点'''
        cur = self.__header

        # while True:

        #     if cur.element == item:
        #         true


if __name__ == "__main__":
    # 创建一个空节点
    SingleLinkList()
