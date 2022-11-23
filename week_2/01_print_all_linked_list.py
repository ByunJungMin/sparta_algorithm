# linked_list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node = Node(3)                          # node 에 Node [3] 저장
first_node = Node(4)                    # first_node에 Node [4] 저장
node.next = first_node                  # node.next 에 [4] 저장
# print(node.next.data)                 # 결과물 4 

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)          # head 노드 생성
    
    def append(self, data):
        if self.head is None:           # head 가 None 일 때 
            self.head = Node(data)      # head 에 Node(data) 대입
            return
       
        cur = self.head                 # cur 에 head노드 저장
        
        while cur.next is not None:     # cur.next 가 None이 아닐 때까지
            cur = cur.next
            print("cur is ", cur.data)
        cur.next = Node(data)           # 마지막 노드에 data 추가

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()