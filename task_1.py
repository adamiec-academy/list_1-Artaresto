def cross(n):
    for i in range(n):
        print(" " * n + n * "*"+ n * " ")
        i=i+1
        if i==n:
            for i in range(n):
                print(n*3*"*")
    for i in range(n):
        print(" " * n + n * "*" + n * " " )
        
