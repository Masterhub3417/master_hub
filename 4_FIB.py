#4_FIB
#解答
#...はファイルの所在を示す


```
def fib(n, k):
    if n <= 2:
        return 1
    else:
        return fib(n-1,k) + k * fib(n-2,k)

if __name__ == "__main__":
    with open(".../rosalind_fib.txt", 'r') as f:
        n, k = f.readline().strip().split(" ")
        print(fib(int(n), int(k)))
```


#模範解答1
#
```
from math import sqrt

def fib_rabbits(n, k):
    d = (-1)**2 - 4 * 1 * (-k)
    f_n = (1/sqrt(d))*((1+sqrt(d))/2)**n - (1/sqrt(d))*((1-sqrt(d))/2)**n
    return int(f_n)

print(fib_rabbits(5, 3))
```



#模範解答2
#
```
fibocache = {}
def fibo(n,k):
    if n == 2 or n == 1:
        return 1
    if (n,k) not in fibocache:
        fibocache[(n,k)] = fibo(n-1,k) + fibo(n-2,k) * k
    return fibocache[(n,k)]

print ( fibo( 5, 3) )

```


#模範解答3
#
```
def fib(n,k):
    if n < 2:
        return n
    else:
        return fib(n-1,k)+(fib(n-2,k)*k)
    
print(fib(5,3))
```
