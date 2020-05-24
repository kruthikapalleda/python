#Given a string, write a program to count the occurrence of Lowercase characters, Uppercase characters, Special characters and Numeric values.

def Count(str):
    upper, lower, number, special = 0, 0, 0, 0
    for i in range(len(str)):
        if str[i] >= 'A' and str[i] <= 'Z':
            upper += 1
        elif str[i] >= 'a' and str[i] <= 'z':
            lower += 1
        elif str[i] >= '0' and str[i] <= '9':
            number += 1
        else:
            special += 1
    print('Upper case :',upper)
    print('Lower case :',lower)
    print('Numbers :',number)
    print('Special case :', special)

str="@(Kcgh652SD!%sdd"
Count(str)

