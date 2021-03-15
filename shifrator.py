action = int(input('1 - зашифровать, 2 - расшифровать\n'))
shifr=''
if action == 1:
    text = input('Введите текст для шифрования\n')
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    secret_key = 3
    for i in text:
        if alphabet.find(i)+secret_key<=len(alphabet):
            shifr = shifr + alphabet[alphabet.find(i)+secret_key]
        if alphabet.find(i)+secret_key>len(alphabet):
            shifr = shifr + alphabet[(alphabet.find(i)+secret_key)%len(alphabet)]
    print(shifr)



