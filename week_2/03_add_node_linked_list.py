# index 번째에 노드 추가

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0

        while count < index:
            node = node.next        # node에 다음번째 node를 저장
            count += 1              # node의 index번째 증가
        return node

    def add_node(self, index, value):
        new_node = Node(value)      # new_node에 새로 입력할 Node 저장

        if index == 0:              # 만약 0번째 인덱스에 추가를 하려면
            new_node.next = self.head   # new_node 다음이 헤드 노드라는걸 알기위한 것
            self.head = new_node    # head node에 new_node 저장
            return

        node = self.get_node(index-1) # index 번째 node에 저장하기 위해서 index -1 번째 node 저장
        new_node = Node(value)      # new_node에 새로 입력할 Node 저장
        next_node = node.next       # next_node에 현재 있는 node.next를 저장
        node.next = new_node        # node에 다음번째에 new_node 저장
        new_node.next = next_node   # 새로운 node의 다음번째에 기존 next_node 저장
        


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.add_node(0,6)
linked_list.print_all()