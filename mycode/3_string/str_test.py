'''
문자열 관련 내용들
'''
# escape 문자
greet = 'Hello' * 4 + '\n'
end = '\tGood \'Bye\' !!'
end2 = "\t Good 'Morning' ??"
print(greet + end + end2)

# bool 타입과 str 타입
is_flag = False
my_str = 'False'
print(type(is_flag), type(my_str))
if not is_flag:
    print(my_str)

# 문자열 인덱스(오프셋)
#           012345678910
greeting = 'hello world'
print('문자열 길이 ', len(greeting))
# c언어 스타일
print('파이썬 %s' % greeting)
print('문자열 길이 %i' % len(greeting))

print('문자열 길이 {0}, 0번째 인덱스 값은 {1}'.format(len(greeting), greeting[0]))
print('0번째 인덱스값은 {1} , 문자열의 길이 {0}'.format(len(greeting), greeting[0]))
# 3.6 버전이후
print(f'문자열 길이 {len(greeting)}, 1번째 인덱스 값은 {greeting[1]}')

# IndexError: string index out of range
# print(greeting[12])

# 문자열 인덱스 슬라이싱 [start:end:step] step은 default 로 1이다. (end값은 exclusive )
print(f'greeting[0:5] = {greeting[0:5]}') #01234
print(f'greeting[6:11] = {greeting[6:11]}') #678910
print(f'greeting[6:] = {greeting[6:]}') #6이후 부터
print(f'greeting[:5] = {greeting[:5]}') #5이전
print(greeting, greeting[:])
print(greeting[::2])  #hlowrd
# 음수값의 인덱스
print(f'greeting[-1:] = {greeting[-1:]}')
print(f'greeting[-2:] = {greeting[-2:]}')
# 문자열이 역순으로 바뀐다
print(f'greeting[::-1] = {greeting[::-1]}')

# 문자열 여러가지 함수들
word = 'Good manufacturing Practice Good'
print(f'대문자로 변환 = {word.upper()}')
result = word.upper()
print(word, '  ', result)
print(f'소문자로 변환 = {word.lower()}')
print(word.title())
print(word.find('G'))
print(word.rfind('G'))
print(word.count('m'))
print(word.count('G'))
word_list = word.split()
print(word_list, type(word_list))
word2 = 'Good/manu/facturing/Practice/Good'
print(word2.split('/'))

word3 = ' hello python '
print(len(word3), len(word3.strip()), word3.strip())
print(len(word3.rstrip()), word3.rstrip())

print(word.startswith('G'))
print(word.endswith('G'))

for val in word:
    print(val, word.count(val))

print(word_list)
for w in word_list:
    print(w)