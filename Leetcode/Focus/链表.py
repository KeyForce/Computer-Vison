class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def len(self):
        #功能：输入头节点，返回链表长度
        curr = self.head
        counter = 0
        while curr:
            counter += 1
            curr = curr.next
        return counter

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
a = LinkedList(head)
print(a.len())

