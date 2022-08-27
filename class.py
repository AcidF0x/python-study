class className:
    shareValue = 100
    """
    해당 클래스의 인스턴스 들이 다 공유하는 클래스 변수
    이거 조금 웃기게 동작한다. 코틀린의 컴패니언 같은 느낌인데
    인스턴스로 접근하는것이 아니라 클래스명으로 접근한다
    """

    def __init__(self): # 생성자
        self.__number = 123 
        """
        private 속성이라는 뜻으로 __를 붙인다 하지만 IDE를 위한 관습적? 키워드로
        실제로 접근이 가능하다 파썬은 은닉화를 지원하지 않는듯 하다
        """
    def increase(self):
        self.__number += 1
    def decrease(self):
        self.__number -= 1
    def getNumber(self):
        return self.__number

class childClass(className):
    pass #상속시 오버라이딩할 내용이 없다면 pass를 써줘야한다 뭔가 귀여운듯?

class child(className):
    def increase(self):
        super().increase()
        super().increase() # super로 부모접근이 가능하다



test = className()
test.increase()
test.decrease()
print(test.getNumber())

className.shareValue = 2000 # 이렇게 쓰면 안되겠지? 초기화 시점은 언제인지?
print(className.shareValue) 


test2 = child()
test2.increase()
print(test2.getNumber())



