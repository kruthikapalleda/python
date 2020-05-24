def first_non_occurence(str1):
    my_dict = {}
    for i in range(0,len(str1),1):
        if str1[i] in my_dict.keys():
            my_dict[str1[i]] = my_dict[str1[i]] + 1
        else:
            my_dict[str1[i]] = 1
    print(my_dict)

    for k,v in my_dict.items():
        if v == 1:
            print("First non Repeated occurence is :", str(k))
            break

if __name__ == '__main__':
    str1 = "cccbbbainnntc"
    first_non_occurence(str1)