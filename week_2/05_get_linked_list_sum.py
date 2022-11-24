# 두 링크드 리스트의 합계

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        if self.head is None:          
            self.head = Node(value)      
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

def get_linked_list_sum(linked_list_1, linked_list_2):
        sum_1 = _get_linked_list_sum(linked_list_1)             # linked_list_1 의 합계를 저장
        sum_2 = _get_linked_list_sum(linked_list_2)             # linked_list_2 의 합계를 저장

        return sum_1 + sum_2

def _get_linked_list_sum(linked_list):
        linked_list_sum = 0                                            
        head = linked_list.head                                 # head 에 linked_list의 head값을 저장
        while head is not None:
            linked_list_sum = linked_list_sum * 10 + head.data  # 6 + 7 + 8 을 하는게 아닌 0*10 + 6, 6*10 + 7, 67*10 + 8 연산
            head = head.next                                    
        return linked_list_sum

linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

result = get_linked_list_sum(linked_list_1, linked_list_2)
print(result)