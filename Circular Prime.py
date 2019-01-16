import sys
num = input('Enter a number:')
l=[]

def find_prime(num):
    for i in range(2,num//2):
        if num%i==0:
            return False
    return True

for char in num:
    l.append(char)
print(l)
r=0
n=''
m=0
d = []
for i in range(0,len(l)):
    m=0
    n=''
    for j in range(0,len(l)):
       n+=l[m+i]
       m+=1
       if m+i>=len(l):
           m=-i
    d.append(int(n))
print(d)

sys.setrecursionlimit((max(d)//2))
for i in range(0,len(d)):
    print(d[i],' is prime? ',find_prime(d[i]))
