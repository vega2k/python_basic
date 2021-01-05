# line comment
'''
    block comment
'''

def add(n1, n2=20):
    print(n1, n2)
    return n1 + n2

print('더하고 싶은 숫자를 입력하세요')
value1 = int(input())
print(type(value1))
result = add(value1)
print(result)