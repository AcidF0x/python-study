# 파이썬은 덕타이핑을 사용하므로 이터러블 인터페이스가 따로 존재하지않는다
# 고로 interable한 동작하게만 하면 된다..

from operator import index


class Animals:
    def __init__(self) -> None:
        self.animalList = ["duck", "dog", "cat", "cow", "snake", "bug"]
        self.cursor = 0 
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cursor < len(self.animalList) - 1:
            self.cursor += 1
            return self.animalList[self.cursor]
        else:
            raise StopIteration


for i in Animals():
    print(i)