'''name = 'inginirium'
for i in range(len(name)):
    print(name[i], end=' ')

for letter in name:
    print(letter, end=' ')

for a in range(4):
    print(name[a])

print(name[0:4:1])
print(name[4:0:-1])
print(name[:])
print(name[::-1])

print(chr(125))
print(ord('%'))
print(chr(ord('a') + 4)) '''


'''message = input('введите сообщение, которое надо зашифровать')
for letter in message:
    print(ord(letter), end=' ')'''


message = input('введите сообщение, которое надо зашифровать')
i = int(input('на сколько символов перенос?'))

for letter in message:
    print((chr(ord(letter) + i)), end=' ')







