def non_repeated(string):
    if (len(string)>2):
        my_res = string[0]
        index = 0

        for i in range(1,len(string),1):
            if string[i] != my_res[index]:
                index = index + 1
                my_res = my_res + string[i]
        print(my_res)
    else:
        print("Enter atleast two characters to compare :")

if __name__ == '__main__':
    string = "aaabbccdddeef"
    #string = ""
    non_repeated(string)