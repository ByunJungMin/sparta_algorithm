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

    def get_kth_node_from_last(self, k):
        slow = self.head                            # k길이만큼 떨어진 노드
        fast = self.head                            # 먼저 도착할 노드
        for i in range(k):
            fast = fast.next                        # k의 길이만큼 앞으로 가라
        
        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow                                 # 결과적으로 k의 길이만큼 slow 노드가 뒤에 있으므로 뒤에서 두번째 노드 출력


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  