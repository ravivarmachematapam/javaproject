
n = int(input("enter a number: "))
for i in range(2,n):
    count=0
    for j in range(2,i):
        if i%j==0:
            count=+1
            break
    if count==0:
        print(i ,end=" ")


n = int(input("\nenter a number :"))
count = 0
for i in range(2,n) :
    if n % i == 0:
        count =+1
        break
if count == 0:
    print(n," is a prime number")
else :
    print(n," is not a prime number")