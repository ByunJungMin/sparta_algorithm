# index 번째 노드 삭제

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
            node = node.next        
            count += 1             
        return node
    def add_node(self, index, value):
        new_node = Node(value)      

        if index == 0:              
            new_node.next = self.head   
            self.head = new_node   
            return

        node = self.get_node(index-1) 
        new_node = Node(value)    
        next_node = node.next    
        node.next = new_node        
        new_node.next = next_node  
        
    def delete_node(self, index): 
        if index == 0:                  # index 가 0이라면
            self.head = self.head.next  # head 의 node에 head의 다음번째 node 저장
            return

        node = self.get_node(index-1)   # index 번째 node 를 node에 저장
        node.next = node.next.next      # node 의 next 를 node의 next.next 값으로 저장


        
          
       


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.add_node(1,6)
linked_list.delete_node(1)
linked_list.print_all()
