class TooBigNumError(Exception):
    def __init__(self,val):
        self.val = val

    def __str__(self):
        return 'too big number {}. use 1 ~ 10!'.format(self.val)


def user_defined_exception():
    num = int(input('1부터 10 사이의 정수를 입력하세요 :'))
    if num > 10:
        raise TooBigNumError(num)
    print('숫자 {} 를 입력하셨군요'.format(num))

user_defined_exception()