while True:
    n = int(input('Enter te no. of lines: '))
    for i in range(n+1):
        for j in range(n+1):
            if j <= i and j >= (n-i) or j >= i and j <= (n-i) and j <= n:
                print("* ", end = "")
            else:
                print("", end = "  ")
        print("\r")
