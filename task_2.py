def chess_board(n, k):
    even_odd = 0
    for i in range(n*2):
            if even_odd == 0:
                for j in range(k):
                    print(((" "+"#")*k)*n, end="\n")
                even_odd = 1
            else:
                for j in range(k):
                    print((("#"+" ")*k)*n, end="\n")
                even_odd = 0
                
"""
def chess_board(n, k):
    for i in range(k):
        for j in range(n):
            if (i + j) % 2 == 0:
                print(("  "+"##")*n, end="\n")
                print(("  "+"##")*n, end="\n")

            else:
                print(("##"+"  ")*n, end="\n")
                print(("##"+"  ")*n, end="\n")
"""
