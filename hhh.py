
ls = [1,2]
for num in range(2, 1000):
    # prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            ls.append(num)
with open('other2.txt',mode='w+') as f:
    f.write(str(ls))
    f.seek(0)
    print(f.read())

def ns(n):
    squaresum = 0
    while (n):
        squaresum += (n % 10) * (n % 10)
        n = int(n / 10)

    return squaresum
l=list()
def ishappy(n):
    n1=n
    n2=n
    while(True):
        n1=ns(n1)
        n2=ns(ns(n2))
        if(n1!=n2):
            continue
        else:
            break
    return (n1 ==1)


for i in range(1000):
    if (ishappy(i)):
        l.append(i)

    else:
        continue

with open('one1.txt',mode='w+') as f:
    f.write(str(l))
    f.seek(0)
    print(f.read())
hh=[]
for i in l :
    if i in ls:
        hh.append(i)
print(hh)