'''def print_sum_two_nums(num_1, num_2):
    result = num_1 + num_2
    return result


summa = print_sum_two_nums(123, 321)
print(summa)'''

'''def coordinates(x, y):
    if x > 0 and y > 0:
        print('1')
    elif x > 0 and y < 0:
        print('4')
    elif x < 0 and y > 0:
        print('2')
    elif x < 0 and y < 0:
        print('3')
    else:
        print('нет плоскости')

coordinates(3, -5)'''

def ask_password():
    password = 234
    for a in range(0, 3, 1):
        user_password = int(input('Введите пароль'))
        if user_password == password:
            break
        else:
            continue


ask_password()

