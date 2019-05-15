def fibo(a,b,n):
    if(n==0):
        return b;
    else:
        return fibo(b,b**2+a,n-1)
x=raw_input()
x=x.split()
print fibo(int(x[0]),int(x[1]),int(x[2])-2)