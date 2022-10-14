def cross(n):
    for i in range(n):
        print(" " * n + n * "*")
        i=i+1
        if i==n:
            for i in range(n):
                print(n*(n-1)*"*")
    for i in range(n):
        print(" " * n + n * "*")
