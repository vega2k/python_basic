# 선수명, 선수 포지션, 선수 등번호
names = ['홍길동', '박지성', '손흥민', '둘리', '파이썬']
positions = ['DF', 'MF', 'GK', 'DF', 'WF']
back_numbers = [5, 10, 20, 30, 15]

# Class 없이 여러명의 선수정보를 2차원 배열에 저장하기
for na,po,ba in zip(names,positions,back_numbers):
    print(na,po,ba)

players = [[name,position,back_number] for name, position, back_number in zip(names,positions, back_numbers)]
#print(players)
player1 = players[0]
# back_number 를 변경
player1[2] = 20
#print(player1)

# SoccerPlayer 클래스를 import
# from 팩키지명.모듈명  import 클래스명 or 함수명
from mycode.oop.python_class import SoccerPlayer

player = SoccerPlayer('dooly','MF', 10)
print(player)
print(player.back_number)

players_obj = [SoccerPlayer(name, position, back_number) for name, position, back_number in zip(names,positions, back_numbers)]
print(players_obj)
player1 = players_obj[0]
# back_number 변경
player1.change_back_number(30)
print(player1)





