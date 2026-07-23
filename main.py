
left = 20
right = 20
while True:
    print( " " * left + "()" + " " * right)
    if input() == "a":
        left -= 1
        right += 1
    elif input() == "d":
        left += 1
        right -= 1