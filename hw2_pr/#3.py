#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
num = input('write a number: ')
sum = 0
for i in num:
    if i != '.':
        sum += int(i)
print(sum)
