text=input('Введите тeкст:')

word=''
reverse_word=''
letter=''

for simvol in text:

    if simvol != ' ':
        word += simvol
    else:
        if word != '':
            if reverse_word == '':
                reverse_word = word
            else:
                reverse_word=word + ' ' + reverse_word
            word=''

if word!='':
    if reverse_word == '':
        reverse_word = word
    else:
        reverse_word = word+' '+reverse_word

print(f'Обратный порядок слов:{reverse_word}')

for character in text:
    
    if character!=' ':
       if letter == '':
            letter=character
       else:
           letter=character + letter
    else:
        if letter == '':
            letter = character
        else:
            letter = character + ' ' + letter

print(f'Обратный порядок букв:{letter}')
