def remove_duplicates(l):
    my_dict = {}
    #res =l.split()
    #print(res)
    for i in range(0,len(l),1):
        if l[i] in my_dict.keys():
            my_dict[l[i]] = my_dict[l[i]] + 1
        else:
            my_dict[l[i]] = 1

    print(my_dict)

    unduplicate_list = []
    for k, v in my_dict.items():
        if v == 1:
         unduplicate_list.append(k)
    print(unduplicate_list)


if __name__ == '__main__':
    #l = "aaababb to be"
    l = ['apple','apple','carrot']
    remove_duplicates(l)