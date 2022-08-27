from calendar import c


class className:
    shareValue = 100
    """
    해당 클래스의 인스턴스 들이 다 공유하는 클래스의 속성
    이거 조금 웃기게 동작한다. 코틀린의 컴패니언 같은 느낌인데
    인스턴스로 접근하는것이 아니라 클래스명으로 접근한다
    """
    def __init__(self): # 생성자
        self.__number = 123 
        """
        private 속성이라는 뜻으로 __를 붙인다
        __로 선언한경우 네임 맹글링을 통해 _클래스명__number로 변경이 된거라 사실 접근이 가능함 *
        이름을 바꿔버리는 원리라 해당 이름으로 접근이 어렵게 만드는 원리

        """
    def increase(self):
        self.__number += 1
    def decrease(self):
        self.__number -= 1
    def getNumber(self):
        return self.__number
    def changeShareValue(self, value):
        # 클래스 속성 접근시 이런식으로 클래스 명으로 접근하거나 클래스 메소드로 접근한다
        className.shareValue = value
    @classmethod
    def changeShareValue2(cls, value):
        """
        클래스 메소드
        @classmethod 데코레이터를 사용하여 self로 인스턴스를 전달하는 대신 클래스를 전달 받는다
        static과 동일하게 인스턴스화 하지않아도 접근이 가능하지만 static과 다르게 클래스 속성에 접근이 가능하다
        """
        cls.shareValue = value
    @staticmethod
    def sayHi():
        return "HI!!"

    

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
print(test._className__number) ## 맹글링 (__ 붙인것)은 접근이 요렇게 접근가능함


className.shareValue = 2000 # 클래스 속성 접근
print(className.shareValue) 

test.changeShareValue(111)
print(className.shareValue)


test.changeShareValue2(44444444)
# 또는
className.changeShareValue2(555555555)
print(className.shareValue)

test2 = child()
test2.increase()
print(test2.getNumber())


print(className.sayHi())
print(test2.sayHi())