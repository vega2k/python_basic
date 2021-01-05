def my_func():
    print(param)
    param = 'Modified by my_func'
    print(id(param))
    
#함수 밖에서 선언한 변수이므로 전역변수(Global Variable)이다.
param = 'Create from outside'
my_func()
print(param)
print(id(param))