def compress(str1):
    res_str = ""
    my_dict = {}

    for i in range(0,len(str1),1):
        if str1[i] in my_dict.keys():
            my_dict[str1[i]] = my_dict[str1[i]] + 1
        else:
            for k,v in my_dict.items():
                res_str = res_str + str(k) + str(v)
               #res_str = res_str + str(k)
            my_dict={}
            my_dict[str1[i]] = 1

    #to append last char
    for k, v in my_dict.items():
        res_str = res_str + str(k) + str(v)
        #res_str = res_str + str(k)

    print(res_str)
    print(my_dict)

if __name__ == '__main__':
    str1 = "aaabbbcacdef"
    compress(str1)