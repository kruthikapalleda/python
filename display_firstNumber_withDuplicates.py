def duplicate_group(l):
    if len(l) > 1 :
        my_dict = {}

        for i in range(0,len(l),1):
            if l[i] in my_dict.keys():
                my_dict[l[i]] = my_dict[l[i]] + 1
            else:
                my_dict[l[i]] = 1

        for k ,v in my_dict.items():
            if v >= 2 :
                print("First duplicate number is : ", str(k))
                break

if __name__ == '__main__':
    l = [0,3,2,1,1,4,6]
    duplicate_group(l)
