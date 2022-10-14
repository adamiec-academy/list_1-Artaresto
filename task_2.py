def chess_board(n, k):
    for i in range(k):
        for j in range(n):
            if (i + j) % 2 == 0:
                print(("  "+"##")*n, end="\n")
                print(("  "+"##")*n, end="\n")

            else:
                print(("##"+"  ")*n, end="\n")
                print(("##"+"  ")*n, end="\n")
                
