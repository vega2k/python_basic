class Dog:
    tricks = []
    def __init__(self,name):
        self.name = name

    def add_trick(self,trick):
        self.tricks.append(trick)

fido = Dog('Fido')
buddy = Dog('buddy')
fido.add_trick('구르기')
print(fido.tricks)
buddy.add_trick('두 발로 서기')
buddy.add_trick('죽은 척 하기')
print(buddy.tricks)