def display_median(l1,l2):
    my_list = []

    for i in range(0,len(l1),1):
        my_list.append(l1[i])
    print(l1)
    for i in range(0,len(l2),1):
        my_list.append(l2[i])
    print(l2)

    sum = 0

    for i in range(0,len(my_list),1):
        sum = sum + my_list[i]
        median = sum/len(my_list)
    print(sum)
    print("Median of the list is : ", median)

if __name__ == '__main__':
    l1 = [1,2,3,4]
    l2 = [1,2,7,8]
    display_median(l1,l2)