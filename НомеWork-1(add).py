# 1-е доп. задание
x = 0
n = 0
result = []
while n != 30:
    n += 1
    x += 1
    if x % 3 == 0 and x % 5 != 0:
       result.append('Fizz')
    elif x % 3 != 0 and x % 5 == 0:
        result.append('Buzz')
    elif x % 3 == 0 and x % 5 == 0:
        result.append('Fizz Buzz')
    else:
        result.append(x)
print(result)

# 2-е доп. задание
x = '1011101110111011101110111011101110111011'
a = 100 # выбираем произвольно
b = 100 # выбираем произвольно
for n in range(3, a):
    l = []
    for i in range(-1, b, n):
        l.append(x[i+1:i+n+1])
    l = list(filter(lambda a: a != '', l))
    if len(set(l)) == 1:
        print('Периодичность сигнала =', n)
        break # break'ом мы оставляем минимальное значение периодичности

# 3-е доп. задание
x = 'testing'
if len(x) % 2 == 1:
    print(x[int((len(x)-1)/2):int((len(x)-1)/2)+1])
else:
    print(x[int((len(x)/2)-1):int((len(x)/2)-1)+2])
