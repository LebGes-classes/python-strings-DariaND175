text=input('Введите тeкст:')

alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
k=0
word=''
count=0

if '.' in text:
    text=text[:text.index('.')+1]

for symbol in text:

    if symbol not in ' ,' and count <= 20:
        word+=symbol
        count+=1
    else:
        if count > k:
            k = count
        count = 0

if count > k:
    k = count
    count=0

result=''
word_len=0

for ch in text:

    if ch in alphabet_lower or ch in alphabet_upper:
        if word_len>=20:
            result+=' '
            word_len=0
        if ch in alphabet_lower:
            new_index=(alphabet_lower.index(ch)+k)%26
            result+=alphabet_lower[new_index]
        else:
            new_index=(alphabet_upper.index(ch)+k)%26
            result+=alphabet_upper[new_index]
        word_len += 1
    else:
        result+=ch
        word_len=0

print(f'''Зашифрованный текст: 
{result}''')
