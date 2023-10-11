
                                              #Задание первое 
 
a = int(input("Введите число, и нажмите Enter "))

if ((a%2) != 0) and ((a/2)>0):

 print("положительное нечетное число")

if (a%2 == 0) and ((a/2)>0):

 print("положительное четное число")

elif (a%2 == 0) and ((a/2)<0):

 print("отрицательное четное число")

elif (a%2 != 0) and ((a/2)<0):

 print("отрицательное нечетное число")

elif (a/2 == 0):

 print("нулевое число")


                                               #Второе задание

slovo = input('Введите слово с гласными буквами: ')

eg=slovo.count('e') # считает количество гласных e

ag=slovo.count('a') # считает количество гласных a

ig=slovo.count('i') # считает количество гласных i

ug=slovo.count('u') # считает количество гласных u

og=slovo.count('o') # считает количество гласных o

schetglas=eg+ag+ig+ug+og # суммирует гласные

print("всего гласных",schetglas) #выводит количество гласных

print("всего согласных",len(slovo)-schetglas)  # считает сколько букв в слове и минусует от общего количества букв гласные, выводит количество согласных
if (eg==0):

 print ("гласной e в слове нет")

else:

 print("e=",eg)

if (ug==0):

 print ("гласной u в слове нет")

else:

 print("u=",ug)

if (og==0):

 print ("гласной o в слове нет")

else:

 print("o=",og)

if (ag==0):

 print ("гласной a в слове нет")

else:

 print("a=",ag)

if (ig==0):

 print ("гласной i в слове нет")

else:

 print("i=",ig)                                               

                                               #Задание третье

minSumInvestment = int(input("Минимальная сумма инвестиций:"))
usdIvan = int(input("Колличество денег у Ивана:"))
usdMike = int(input("Колличество денег у Майка:"))

if (minSumInvestment <= usdIvan) and (minSumInvestment <= usdMike):
 print("Оба могут вложиться!")
elif (minSumInvestment > usdMike) and (minSumInvestment <= usdIvan):
 print("Только Иван может")
elif (minSumInvestment <= usdMike) and (minSumInvestment > usdIvan):
 print("Только Майк может")
elif (usdIvan <= minSumInvestment) and (usdMike <= minSumInvestment) and ((usdIvan + usdMike)>= minSumInvestment):
 print("Вместе могут")
elif(usdIvan <= minSumInvestment) and (usdMike <= minSumInvestment) and ((usdIvan + usdMike) <= minSumInvestment):
 print("Никто не может")