#Check if input is plaindrome or not
input_str = input("Give an input string: ")

length = len(input_str)

if int(length%2) == 0:
    for i in range(int(length/2)):
        if input_str[i] == input_str[-(i+1)]:
            continue
        else:
            print("False")
            break
    else:
        print("True")

else:
    for i in range(int(length/2)+1):
        if input_str[i] == input_str[-(i+1)]:
            continue
        else:
            print("False")
            break
    else:
        print("True")