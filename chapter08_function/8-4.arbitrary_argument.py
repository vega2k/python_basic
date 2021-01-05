def introduce_your_family(name,*family_names, **family_info):
    print('제이름은 ',name,'입니다.')
    print('제 가족들은 이름은 아래와 같아요')

    for family_name in family_names:
        print(family_name)
    print('-'*40)

    for key in family_info:
        print(key,':',family_info[key])


introduce_your_family('홍길동','영희','지운','가영',집='용인',가훈='행복하게 살자!')


def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earch","mars","venus"))
print(concat("earch","mars","venus",sep="."))
