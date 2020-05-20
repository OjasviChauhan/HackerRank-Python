if __name__ == '__main__':
    s = input()
    for j in s:
        k = ""
        if(j.isalnum()):
            k = "True"
            print(k)
            break
    if(k != "True"):
        print("False")

    for j in s:
        k = ""
        if(j.isalpha()):
            k = "True"
            print(k)
            break
    if(k != "True"):
        print("False")

    for j in s:
        k = ""
        if(j.isdigit()):
            k = "True"
            print(k)
            break
    if(k != "True"):
        print("False")

    for j in s:
        k = ""
        if(j.islower()):
            k = "True"
            print(k)
            break
    if(k != "True"):
        print("False")

    for j in s:
        k = ""
        if(j.isupper()):
            k = "True"
            print(k)
            break
    if(k != "True"):
        print("False")
