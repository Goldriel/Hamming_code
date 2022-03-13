def chek_input(num):
    i = 0
    while i < len(num):
        if ord(num[i]) >= 0 and ord(num[i]) <= 255:
            i += 1
        else:
            print("unsupported character")
            exit()