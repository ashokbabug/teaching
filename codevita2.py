x = int(input())
def factorialOfNumber(n):
    if n==0 or n==1:
        return 1
    return n*factorialOfNumber(n-1)

s = 0
numb = 2
for i in range(2,x+1):
    if numb%2==0:
        s+=(1/factorialOfNumber(i))
    else:
        s-=(1/factorialOfNumber(i))
    numb+=1

print(factorialOfNumber(x)-(int(factorialOfNumber(x)*s)),end='')