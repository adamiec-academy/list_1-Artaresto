def chess_board(n, k):
    even_odd = 0
    for i in range(n):
            if even_odd == 0:
                for j in range(k):
                    print(("  "+"##")*n, end="\n")
                even_odd = 1
            else:
                for j in range(k):
                    print(("##"+"  ")*n, end="\n")
                even_odd = 0
