def factorial(n):
    silnia = 1
    for i in range(n,n +1):
        if n==0 or n==1:
            return 1
        else:
            for i in range (2, n+1):
                silnia = silnia*i
            return silnia           

def report():
    for j in range(101):
        silnia = factorial(j)
        dlugosc = len(str(silnia))

        print( f"{str(j):>3}! is {str(dlugosc):>3} digits long")
