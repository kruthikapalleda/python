def string_reverse_word(str1):
    string_arr=str1.split(' ')
    res_string = ""

    for i in range(0,len(string_arr),1):
        result = my_reverse(string_arr[i])
        res_string = res_string + " "+ result
    print(res_string)

def my_reverse(str1):
    res_string = ""
    for i in range(len(str1)-1,-1,-1):
        res_string = res_string + str1[i]
    return res_string

if __name__ == '__main__':
    str1 = "I am apple"
    string_reverse_word(str1)
    my_reverse(str1)