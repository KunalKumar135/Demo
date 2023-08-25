n=int(input())
n1=0
n2=0
c=0
if(n<1):
    print("Please give a positive number")
elif(n==1):
    print("The fibonacii series of",n,"is",n1)
else:
    while(c<=n):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        c+=1



