'''class Human:
    age = 10
    heigh = 150
    weight = 50

    def say_hello(self):
        print('Hello!')
        print('I am a Human.')

    def say_good_bye(self):
        print('See you!')

john = Human()
frank = Human()
print(john.age)
john.say_hello()
print(frank.heigh)
frank.say_good_bye()'''

class Car:
    def sound(self):
        print('Beep!')

    def long_sound(self):
        print('Beep-beep!')


bus = Car()
bus.sound()
bus.long_sound()

class Button:
    def __init__(self):
        self.clicks = 0

    def click(self):
        self.clicks += 1

    def click_count(self):
        print(self.clicks)

button = Button()
button.click()
button.click()
button.click()
button.click_count()