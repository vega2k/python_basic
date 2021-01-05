def my_func(param):
    #함수내의 param 변수는 지역변수(local variable)
    param = 'Modified by my_func'
    print(param)
    print(id(param))

param = 'Create from outside'
my_func(param)
print(param)
print(id(param))