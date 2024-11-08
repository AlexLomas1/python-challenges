def hollow_pyramid(n):
    n -= 1
    length = n * 2
    for i in range(0,n+1):
        list = [" "] * (length+1)
        if i == n:
            list = ["A"] * (length+1)
        else:
            list[n-i] = "A"
            list[n+i] = "A"
        print("".join(list))

layers = int(input("Number of layers: "))
hollow_pyramid(layers)