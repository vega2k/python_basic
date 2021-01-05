# dict 타입
# dict() , { }
lang_dict = {}
lang_dict2 = dict()
print(type(lang_dict), type(lang_dict2))

# dict에 값을 저장
lang_dict[100] = '자바'
lang_dict[200] = '파이썬'
lang_dict[200] = '텐서플로'
lang_dict[300] = 'PyTorch'
print(lang_dict)

# dict에서 값을 읽기
print(lang_dict[300])
# KeyError: 400
# print(lang_dict[400])
value = lang_dict.get(400)
print(value)
if value:
    print(value)
else:
    print('해당 key의 값이 없음')

for k, v in lang_dict.items():
    print(k, v)

print(200 in lang_dict)
print(400 in lang_dict)
print('자바' in lang_dict.values())

# zip() 함수
days = ['월요일', '화요일', '수요일']
fruits = ['사과', '바나나', '딸기']
coffees = ['아메리카노', '라떼', '모카', '믹스']

print(zip(days, fruits, coffees), type(zip(days, fruits, coffees)))
for day, fruit, coffee in zip(days, fruits, coffees):
    print(day, fruit, coffee)

print(dict(zip(days, fruits)))
print(list(zip(days, coffees)))

for value in list(zip(days, coffees)):
    print(value)

days_tuple = '월요일', '화요일', '수요일'
coffees_tuple = '아메리카노', '라떼', '모카'
print(type(days_tuple))
print(list(zip(days_tuple, coffees_tuple)))
print(dict(zip(days_tuple, coffees_tuple)))

# zip(), range() 함수는 iterable 객체를 반환하기 때문에 값을 확인하려면 for ~ in 구문, list() 함수를 사용한다.
print(range(10))
print(list(range(1, 10, 2)))
