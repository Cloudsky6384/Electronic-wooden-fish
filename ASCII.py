# ASCII化
def encrypt(enter):
    listgo = []
    for x in range(0, len(str(enter))):
        listgo.append(ord(str(enter)[x]))

    return listgo


# ASCII还原
def decrypt(enter):
    go = ''
    for x in enter:
        go += chr(x)

    return go
