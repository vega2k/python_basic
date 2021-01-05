# 사용자 정의 예외 클래스 선언
class NegativePriceException(Exception):
    # constructor 선언
    def __init__(self):
        print("Price can't be Negative")
        raise AttributeError

def calc_price(value):
    price = value * 100
    if price < 0:
        # NegativePriceException 를 강제로 발생시킨다 
        raise NegativePriceException
    return price

print(calc_price(10))
print(calc_price(-10))