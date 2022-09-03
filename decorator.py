# 다른 언어들의 어노테이션 프록시나 리플렉션같은걸 사용안하는건 좀 신기한걸?
# 아주 쉽고 간단하게 주입되는 부분이라 즐겁다
# 우선순위는 실제 함수명과 가장 가까운부분 (아래) 부터 실행되는듯

class User:
    def __init__(self) -> None:
        self.userEmail = "mail@mail.com"
        self.userName = "Admin"
        self.userRole = "Admin"

def injectUser(func):
    print("this is inject user decorator")
    def decorator(*args, **kwargs):
        func(*args, **kwargs, user = User())
    return decorator

def first(func):
    print("this is first decorator")
    def decorator(*args, **kwargs):
        func(*args, **kwargs)
    return decorator

@first
@injectUser
def doSomeThing(a, b, user = None):
    email = user.userEmail if user != None else "-"
    print(f"user {email} and {a+b}")

doSomeThing(a="1", b="2")
