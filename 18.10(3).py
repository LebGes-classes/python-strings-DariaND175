import re


text=input('Введите тeкст:')

text=text.lower()
words=re.findall(r'\b[а-яё]+\b',text)
slovar_word={}

for word in words:

    if word in slovar_word:
        slovar_word[word]+=1
    else:
        slovar_word[word]=1

list_sort_word=[]

for word,count in slovar_word.items():
    list_sort_word.append((word,count))

length=len(list_sort_word)

for proxod in range(length):
    for tek_simvol in range(length-proxod-1):
        word,count=list_sort_word[tek_simvol]
        next_word,next_count=list_sort_word[tek_simvol+1]

        if count<next_count:
            list_sort_word[tek_simvol],list_sort_word[tek_simvol+1]=list_sort_word[tek_simvol+1],list_sort_word[tek_simvol]


max_5=list_sort_word[:5]

for i in range(len(max_5)):
    word,count=max_5[i]

    print(f'{word}-{count}')
