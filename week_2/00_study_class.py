class Person:                                               
    def __init__(self, param_name):     # class를 만들 때 생성자를 설정하기 위해서 만드는 함수
        print('i am created! ', self)   # self 사용 이유 constructor 생성이나 내부에 있는 함수를 만들 때 인자로 자기자신을 넘겨주기 때문
        self.name = param_name          # 자신의 안에 name이라는 변수를 만들고 param_name을 저장

    def talk(self):                     # talk 메소드 생성
        print("안녕하세요, 제 이름은", self.name, "입니다")
    

person_1 = Person("유재석")             # class를 통한 새로운 객체를 만들겠다는 의미
print(person_1.name)
print(person_1)
person_1.talk()
person_2 = Person("박명수")             # () 는 constructor 즉 생성자 이것은 객체를 생성할 때 쓰는 함수
print(person_2.name)
print(person_2)
person_2.talk()