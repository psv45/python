action = int(input('1 - зашифровать, 2 - расшифровать\n'))
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
shifr=''
if action == 1:
    text = input('Введите текст для шифрования\n')
    secret_key = 3
    for i in text:
        if alphabet.find(i)+secret_key<=len(alphabet):
            shifr = shifr + alphabet[alphabet.find(i)+secret_key]
        if alphabet.find(i)+secret_key>len(alphabet):
            shifr = shifr + alphabet[(alphabet.find(i)+secret_key)%len(alphabet)]
    print('Зашифрованное слово:', shifr)
    print('Ключ:', secret_key)
elif action == 2:
    text = input('Введите текст для расшифровки\n')
    secret_key = int(input('Введите ключ\n'))
    for i in text:
        if alphabet.find(i)-secret_key>=1:
            shifr = shifr + alphabet[alphabet.find(i)-secret_key]
        if alphabet.find(i)-secret_key<1:
            shifr = shifr + alphabet[(alphabet.find(i)-secret_key+len(alphabet))%len(alphabet)]
    print('Расшифрованное слово:', shifr)