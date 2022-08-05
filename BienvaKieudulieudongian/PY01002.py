def main():
    a = input()
    b = a.split(" ")
    if int(b[0]) + int(b[2]) == int(b[4]):
        print("YES")
    elif int(b[0]) + int(b[2]) != int(b[4]):
        print("NO")
    
main()
