def introduce_my_car(manufacturer, seats=4, type='sedan'):
    print('내 차는',manufacturer,'에서 제작된',seats,'인승',type,'이다')

#위치 인자값
introduce_my_car('현대')
#키워드 인자값 1개
introduce_my_car(manufacturer='기아')
#키워드 인자값 2개
introduce_my_car(manufacturer='기아',type='SUV')

#순서가 바뀐 키워드 인자값 2개
introduce_my_car(manufacturer='기아',type='SUV')

#위치 인자값
introduce_my_car('아우디',2,'스포츠카')

#unpacking argument
input = {'manufacturer':'현대','seats':9,'type':'승합차'}
introduce_my_car(**input)
