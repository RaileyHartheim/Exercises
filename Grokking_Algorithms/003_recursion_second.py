def recursion(n):
    if n == 1:
        return 1
    else:
        return (str(recursion(n-1)) + " " + str(n))

print(recursion(7))
