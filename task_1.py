def cross(n, shift):
    for i in range(n):
        print(shift * " ", end="")
        print(n * "*")
        i=i+1
        if i==n:
            for i in range(n):
                print(n*(n-1)*"*")
    for i in range(n):
        print(shift * " ", end="")
        print(n * "*")
cross(4, 4)
