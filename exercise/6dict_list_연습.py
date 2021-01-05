users = [{'id':1,'name':'홍길동','email':'hong@mail.com','hp_num':'010-2343-1234'},
         {'id': 2, 'name': '이순신', 'email': 'lee@mail.com', 'hp_num': '010-3333-5555'}]
#users[0] = {'id':1,'name':'hong kildong','email':'hong@mail.com','hp_num':'010-2343-1234'}

users.append({'id': 3, 'name': '장영실', 'email': 'jang@mail.com3', 'hp_num': '010-7777-1233'})
users.append({'id': 4, 'name': '세종대왕', 'email': 'sejong@mail.com3', 'hp_num': '010-4567-1233'})
print(users)

for user in users:
    for key in user.keys():
        print('{} = {} '.format(key, user[key]))

print('items() 사용 ---------------------------------')
for user in users:
    for key, value in user.items() :
        print(f'{key} = {value}')
