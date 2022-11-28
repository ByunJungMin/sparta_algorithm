# stack

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)              # new_head 로 지정할 Node(value) data 저장
        new_head.next = self.head           # new_head 의 다음은 기존의 self.head
        self.head = new_head                # new_head 를 self.head 로 지정
        return

    def pop(self):
        if self.is_empty():                 # 만약 self.head 가 없다면
            return None     
        delet_head = self.head              # 삭제할 헤드에 self.head 저장
        self.head = self.head.next          # self.head 에 기존의 self.head.next 저장
        return  delet_head.data

    def peek(self):                         # 현재 head.data 가 무엇인지 확인
        if self.is_empty():
            return None
        return  self.head.data

   
    def is_empty(self):                     # self.head 가 None 이라면 True 출력
        return  self.head is None


stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
print(stack.pop())
print(stack.is_empty())
