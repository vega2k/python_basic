class SoccerPlayer(object):
    # 생성자 함수 - 객체 생성될때 호출됨
    def __init__(self, name, position, back_number=20):
        # print('생성자 함수 호출됨')
        # 속성들
        self.name = name
        self.position = position
        self.back_number = back_number
    
    # back_number  속성을 변경하는 메서드
    def change_back_number(self1, new_number):
        print("선수의 등번호를 변경합니다 : From %d to %d" % (self1.back_number, new_number))
        self1.back_number = new_number
    
    # 객체주소 대신에 원하는 다른 속성값을 반환 해주는 메서드
    def __str__(self):
        # print('객체의 속성 값을 반환 해주는 메서드')
        return "Hello, My name is %s. I play in %s in center  Back Number %d" % (self.name, self.position, self.back_number)

def main():
    # 객체생성
    jinhyun = SoccerPlayer("Jinhyun", "MF", 10)
    print(jinhyun)

    dooly = SoccerPlayer('둘리', 'GK')
    print(dooly)

    print("현재 선수의 등번호는 :", jinhyun.back_number)
    jinhyun.change_back_number(5)
    print("현재 선수의 등번호는 :", jinhyun.back_number)

# 실행했을 경우에만  main() 함수를 호출해라 ctrl + shift + f10, python python_class.py
# import 한 경우에는 main() 함수가 호출되지 않는다.
if __name__ == "__main__":
    main()