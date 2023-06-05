

stroka1='пара-ра-рам рам-пам-папам па-ра-па-дам'
vowels=['a','e','ё','и','й','o','у','ы','э','ю','я']
phrases=stroka1.split()
if len(phrases)<2:
   print('Количество фраз должно быть больше одной!')
else:
   countVowels=[]

   for i in phrases:
       countVowels.append(len([x for x in i if x.lower() in vowels]))

if len (set(countVowels))==1:
   print('Парам пам-пам')
else:
   print('Пам парам')