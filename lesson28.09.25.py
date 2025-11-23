# state = input('How are you')
# if state == 'sleepy':
#    print('sleep in')
# elif state == 'energy':
#    print('mega energy')
#else:
#    print('start your day!')


#name = input('What is your name?')
#surname = input("What is your surname?")
#age = int(input('what is your age?'))
#if age <= 18:
#    print('ты еще ребенок', name, surname)
#else:
#    print('ты уже взрослый', name, surname)

 #   question = input("Ты нефор? Любишь им быть?")
 #   if question == 'да да':
  #  print('правильно молодец')
  #  elif question == 'нет нет':
  #  print('неправильно, врешь')
 #   elif question == 'нет да':
 #   print('определись')
 #   elif question == 'да нет':
 #   print('зря')
 #   else:
#print('ошибка')

#x = int(input('first number'))
#y = int(input("second number"))
#z = input("symbol")

#    if z == "*":
#        print(x * y)
#    elif z == "+":
#            print(x + y)
#    elif z == "+":
#            print(x + y)
#    elif z == "-":
#            print(x - y)
#   elif z == "/":
#            print(x / y)
#   elif z == "%":
#            print(x % y)
#    else:
#        print('error')

win = [1, 2, 12]
spr = [3, 4, 5]
summer = [6, 7, 8]
aut = [9, 10, 11]

month = int(input('номер месяца'))

if month in win:
    print('зима')
elif month in spr:
    print('весна')
elif month in summer:
    print('лето')
elif month in aut:
    print('осень')
else:
    print("такого месяца нет")

