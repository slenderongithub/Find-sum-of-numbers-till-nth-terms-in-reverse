#WAP to find sum of numbers till nth terms in reverse series: ......5+4+3+2+1=
n=int(input("Enter the number of terms: "))
s=0
for i in range(n,0,-1):
    print(i,end="")
    if(i>1):
        print("+",end="")
    s=s+i
print("=",s)