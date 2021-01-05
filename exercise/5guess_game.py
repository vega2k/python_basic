'''
Guess Game
1)1 부터 100 사이의 값을 랜덤하게 추출한다.
2)사용자로 부터 숫자를 입력받는다.
3)랜덤하게 추출한 숫자와 입력받는 숫자가 같으면 game 종료
  정답을 알려주고, 몇번 만에 맞추었는지도 출력한다.
4)입력받은 숫자 > 랜덤한 숫자 보다 크면
   '숫자가 너무 큽니다'  출력
  입력받은 숫자 < 랜덤한 숫자 보다 작으면
   '숫자가 너무 작습니다' 출력
   if / while 구문 사용
'''
import random
guess_number = random.randint(1,100)
#print(guess_number)
num = input('숫자를 입력하세요 :')
print(int(num))

print('1 부터 100 사이의 숫자를 입력하세요')
input_number = int(input())
print(input_number, '를 입력하셨군요.')

count = 0
while input_number is not guess_number:
    if input_number > guess_number:
        print('숫자가 너무 큽니다')
    else:
        print('숫자가 너무 작습니다')
    count += 1
    input_number = int(input())
else:
    print(count ,'번 만에 맞추셨군요')
    print('입력한숫자= ', input_number,' 정답은= ', guess_number)

