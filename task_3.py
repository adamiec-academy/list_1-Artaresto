def envelope(n):
    
    max_min = 2*n+1
    
    for i in range (max_min):
        for j in range (max_min):
            if i == 0 or i == (max_min-1) or j==0 or j==(max_min-1) or i+j==(max_min-1) or i==j:
                print("*", end="")
            else:
                print(" ", end="")
        
        print()
